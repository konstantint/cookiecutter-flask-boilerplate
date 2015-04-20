# -*- coding: UTF-8 -*-
"""
{{cookiecutter.project}}: PyTest configuration

See https://pytest.org/latest/plugins.html

Copyright {{cookiecutter.year}}, {{cookiecutter.author}}
License: {{cookiecutter.license}}
"""

import pytest, os
from webtest import TestApp

from {{cookiecutter.package}}.app import create_app
from {{cookiecutter.package}} import model


@pytest.yield_fixture
def app():
    os.environ['CONFIG'] = '{{cookiecutter.package}}.config.TestConfig'
    app = create_app()
    model.init_db_tables(app)
    model.init_db_data(app)
    ctx = app.test_request_context()
    ctx.push()
    yield app
    ctx.pop()


@pytest.fixture
def testapp(app):
    return TestApp(app)
