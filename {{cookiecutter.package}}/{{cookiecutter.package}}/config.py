# -*- coding: UTF-8 -*-
"""
{{cookiecutter.project}}: Config module

Copyright {{cookiecutter.year}}, {{cookiecutter.author}}
License: {{cookiecutter.license}}
"""
import logging, os
log = logging.getLogger('{{cookiecutter.package}}.config')


def init_app(app):
    '''
    Configuration initialization logic.
    The default values are first loaded from config.Config.
    Those are then overridden with the values stored in the file pointed by the $CONFIG environment variable.

    For testing, set os.environ['CONFIG'] to '{{cookiecutter.package}}.config.TestConfig' before calling create_app.
    '''

    # First load the default values
    app.config.from_object('{{cookiecutter.package}}.config.Config')

    # Then override with ${CONFIG}, if specified
    if 'CONFIG' in os.environ:
        log.debug('Loading settings from %s' % os.environ['CONFIG'])
        try:
            # Assume CONFIG is a name of a class
            app.config.from_object(os.environ['CONFIG'])
        except:
            # No, perhaps it's a filename then?
            app.config.from_envvar('CONFIG')


class Config(object):
    # Default settings are debug-friendly
    # Make sure to disable all that in production
    DEBUG = True
    ASSETS_DEBUG = True
    SQLALCHEMY_ECHO = True
    DEBUG_SERVER_HOST = '0.0.0.0'
    DEBUG_SERVER_PORT = 5000

    # Database connection: default is to use a db.sqlite file in the package root.
    SQLALCHEMY_DATABASE_URI = 'sqlite:///%s' % os.path.join(os.path.dirname(os.path.abspath(__file__)), '..', 'db.sqlite')

    # Secret key for session authentication.
    # Make sure to set it to something different than the default in your local config
    SECRET_KEY = "<set this to something properly secret>"

    # See assets.py
    USE_CDN_ASSETS = False


class TestConfig(Config):
    DEBUG = False
    ASSETS_DEBUG = False
    SQLALCHEMY_ECHO = False
    DEBUG_SERVER_HOST = '0.0.0.0'
    DEBUG_SERVER_PORT = 5001
    SQLALCHEMY_DATABASE_URI = 'sqlite://'  # In-memory database
    SECRET_KEY = "does not matter"
    USE_CDN_ASSETS = False
    WTF_CSRF_ENABLED = False  # Allows form testing
