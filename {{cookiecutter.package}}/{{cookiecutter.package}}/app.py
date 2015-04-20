# -*- coding: UTF-8 -*-
"""
{{cookiecutter.project}}: App factory.

See: http://flask.pocoo.org/docs/latest/patterns/appfactories/'

Copyright {{cookiecutter.year}}, {{cookiecutter.author}}
License: {{cookiecutter.license}}
"""

from flask import Flask, render_template
from . import config, model, assets, i18n, views


def create_app():
    'App factory.'

    app = Flask(__name__)
    init_app(app)
    return app


def init_app(app):
    'Initialization of app config, followed by registrations of all the extensions and views.'

    # Load config. See config.init_app for config loading logic.
    config.init_app(app)

    # Initialize app-wide extensions
    model.init_app(app)  # Flask-SQLAlchemy
    i18n.init_app(app)   # Flask-Babel
    assets.init_app(app) # Flask-Assets

    # Add views
    views.admin.init_app(app)                       # Flask-Admin
    app.register_blueprint(views.auth.blueprint)    # Flask-Login
    app.register_blueprint(views.main.blueprint)    # Main app views

    # Auto-fix proxy IP address and host
    # Disable if you are not planning to serve this app behind a nginx or apache proxy
    from werkzeug.contrib.fixers import ProxyFix
    app.wsgi_app = ProxyFix(app.wsgi_app)

    # Set up simple error handlers
    @app.errorhandler(404)
    def page_not_found(e):
        return render_template('404.html'), 404

    @app.errorhandler(500)
    def server_error(e):
        return render_template('500.html'), 500


def app_factory(global_config, **local_conf):
    '''
    Entry point for interfacing with PasteDeploy.
    See: http://pythonpaste.org/deploy/#paste-app-factory
    '''
    app = create_app()
    return app.wsgi_app
