# -*- coding: UTF-8 
"""
{{cookiecutter.project}}: Flask-SQLAlchemy models

See: https://pythonhosted.org/Flask-SQLAlchemy/
NB: For larger projects it may make sense to split model into several modules under a .model/ subpackage.

Copyright {{cookiecutter.year}}, {{cookiecutter.author}}
License: {{cookiecutter.license}}
"""
from sqlalchemy import *
from flask.ext.sqlalchemy import SQLAlchemy
from flask.ext.login import UserMixin

db = SQLAlchemy()
Base = db.Model


# By default we define a minimalistic "user" table, necessary for Flask-Login
# Feel free to drop all that along with the whole Flask-Login business if you do not need it.
class User(Base, UserMixin):
    id = Column(Integer, primary_key=True)
    login = Column(String(80), unique=True)
    password = Column(String(64))


# Create database
def init_db_tables(app):
    with app.app_context():
        db.create_all()


# Initialize core db data
def init_db_data(app):
    from werkzeug.security import generate_password_hash

    with app.app_context():
        u = User(id = 0, login='admin', password=generate_password_hash('admin'))
        db.session.add(u)
        db.session.commit()


def init_app(app):
    db.init_app(app)