# -*- coding: UTF-8 -*-
"""
{{cookiecutter.project}}: Flask-Babel integration

The default I18N configuration provided here is fairly useless (and harmless)
See: https://pythonhosted.org/Flask-Babel/

Copyright {{cookiecutter.year}}, {{cookiecutter.author}}
License: {{cookiecutter.license}}
"""
from flask.ext.babel import Babel

def get_locale():
    return 'en'

def init_app(app):
    babel = Babel(app)
    babel.localeselector(get_locale)
