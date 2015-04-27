# -*- coding: UTF-8 -*-
"""
{{cookiecutter.project}}: Main views

Copyright {{cookiecutter.year}}, {{cookiecutter.author}}
License: {{cookiecutter.license}}
"""
from flask import Blueprint, render_template, flash
blueprint = Blueprint('main', __name__, url_prefix='')


# ----------------------------------- Views ------------------------------------- #
@blueprint.route('/')
def index():
    return render_template('index.html')


# ------------ This may be a reasonable place to put stray Jinja template filters needed in the views ------------- #
# Alternatively, you may put them in a separate blueprint in, e.g. views/templatefilters.py
@blueprint.app_template_filter('nvl')  # http://stackoverflow.com/questions/11146619/suppress-none-output-as-string-in-jinja2
def _jinja2_filter_supress_none(val):
    if not val is None:
        return val
    else:
        return ''