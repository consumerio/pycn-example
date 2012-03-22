"""
Flask Documentation:     http://flask.pocoo.org/docs/
Jinja2 Documentation:    http://jinja.pocoo.org/2/documentation/
Werkzeug Documentation:  http://werkzeug.pocoo.org/documentation/

This file creates your application.
"""

import os
from flask import Flask, render_template, request, redirect, url_for
import private
import pycn

app = Flask(__name__)

if 'SECRET_KEY' in os.environ:
    app.config['SECRET_KEY'] = os.environ['SECRET_KEY']
else:
    app.config['SECRET_KEY'] = 'this_should_be_configured'

auth = pycn.OAuth2Handler(
        client_id=private.CLIENT_ID,
        client_secret=private.CLIENT_SECRET,
        redirect_uri=private.REDIRECT_URI
    )


###
# Routing for your application.
###

@app.route('/')
def home():
    """Render website's home page."""
    try:
        connect_url = auth.get_authorization_url()
    except pycn.AuthorizationURLError:
        app.logger.error('Cannot get the authorization URL.')

    return render_template('home.html', connect_url=connect_url)

@app.route('/browse/')
def browse():
    """Render the website's browse page."""
    # Get the "code" value
    code = request.args.get('code', '')

    # Use it to get an access token
    try:
        access_token = auth.get_access_token(code)
    except pycn.AccessTokenError:
        app.logger.error('Error! Failed to get access token.')
        
    api = pycn.API(auth)

    return render_template('browse.html', access_token=access_token, my_profile=api.my_profile())

@app.route('/about/')
def about():
    """Render the website's about page."""
    return render_template('about.html')


###
# The functions below should be applicable to all Flask apps.
###

@app.route('/<file_name>.txt')
def send_text_file(file_name):
    """Send your static text file."""
    file_dot_text = file_name + '.txt'
    return app.send_static_file(file_dot_text)


@app.after_request
def add_header(response):
    """
    Add headers to both force latest IE rendering engine or Chrome Frame,
    and also to cache the rendered page for 10 minutes.
    """
    response.headers['X-UA-Compatible'] = 'IE=Edge,chrome=1'
    response.headers['Cache-Control'] = 'public, max-age=600'
    return response


@app.errorhandler(404)
def page_not_found(error):
    """Custom 404 page."""
    return render_template('404.html'), 404


if __name__ == '__main__':
    app.run(debug=True)
