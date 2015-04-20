# -*- coding: UTF-8 -*-
"""
{{cookiecutter.project}}: Flask-Admin integration

See: https://flask-admin.readthedocs.org/

NB: Initially configured to interoperate with (and thus depend on) Flask-Login and Flask-SQLAlchemy.

Copyright {{cookiecutter.year}}, {{cookiecutter.author}}
License: {{cookiecutter.license}}
"""
from flask import redirect, url_for
from flask.ext.admin import Admin, BaseView, AdminIndexView, expose
from flask.ext.admin.contrib.sqla import ModelView
from flask.ext.login import current_user

from {{cookiecutter.package}}.model import db, User

def init_app(app):
    'Set up Flask-Admin views here'
    
    admin = Admin(app, name='Site Administration', index_view=LoginFriendlyAdminIndexView())
    admin.add_view(SiteConfigView(name='Settings'))
    admin.add_view(UserModelView(User, db.session, category='Models'))


class AdminAccessControlMixin(object):
    '''Configure general admin access authorization details here.
    Make sure this class goes first in the parent list of model classes.
    '''

    def is_accessible(self):
        return current_user.is_authenticated() and current_user.login == 'admin'


class LoginFriendlyAdminIndexView(AdminIndexView):
    'We add the automated redirection to login on the home page of this view for convenience.'
    
    @expose('/')
    def index(self):
        if not current_user.is_authenticated():
            return redirect(url_for('auth.login', next=url_for('admin.index')))
        return super(LoginFriendlyAdminIndexView, self).index()


class UserModelView(AdminAccessControlMixin, ModelView):
    pass


class SiteConfigView(AdminAccessControlMixin, BaseView):
    @expose('/')
    def index(self):
        return self.render('admin/site_config.html')
