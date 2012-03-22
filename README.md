=====================
pycn example
=====================

By @audreyr.

This is a sample Flask project that demonstrates use of pycn, the Python library for accessing the Consumer Notebook API.

Running it locally
------------------

These instructions assume that you have pip, virtualenv, and virtualenvwrapper installed.

In your terminal::

    $ git clone https://github.com/consumernotebook/pycn-example.git
    $ cd pycn-example
    $ mkvirtualenv pycn-example
    $ pip install -r requirements.txt

To run it in debug mode locally::

    $ python runserver.py

In your browser, go to http://127.0.0.1:5000/

Note: you can also run it with Foreman, but you won't get the debugger::

    $ foreman start

Deploying it on Heroku
----------------------

Follow the deployment instructions at https://github.com/zachwill/flask_heroku.  

Credits
-------

Based on the code from the [Flask Heroku](https://github.com/zachwill/flask_heroku) project.
