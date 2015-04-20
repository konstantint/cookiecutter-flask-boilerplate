# -*- coding: UTF-8 -*-
"""
{{cookiecutter.project}}: Flask-Login integration

See: https://flask-login.readthedocs.org/

NB: Depends on the existence of {{cookiecutter.package}}.model.db and {{cookiecutter.package}}.model.User.
The latter must be a Flask-Login-compatible User model. This can be changed, if necessary

Copyright {{cookiecutter.year}}, {{cookiecutter.author}}
License: {{cookiecutter.license}}
"""
from flask import Blueprint, render_template, flash, redirect, request, url_for, current_app
from flask.ext.login import LoginManager, login_user, logout_user, login_required
from flask_wtf import Form
from wtforms import fields, validators
from werkzeug.security import check_password_hash

from {{cookiecutter.package}}.model import db, User

blueprint = Blueprint('auth', __name__, url_prefix='/auth')


def init_blueprint(setup_state):
    '''Set up Flask-Login on blueprint registration'''
    
    app = setup_state.app
    login_manager = LoginManager()
    login_manager.init_app(app)
    login_manager.login_message = u"Please, log in to access this page"
    login_manager.login_message_category = "info"

    # Create user loader function
    @login_manager.user_loader
    def load_user(user_id):
        return db.session.query(User).get(user_id)

blueprint.record_once(init_blueprint)


# ----------------------------------- Login/Logout forms and views, "blueprint"-style ------------------------------------- #
class LoginForm(Form):
    login = fields.StringField(validators=[validators.DataRequired()])
    password = fields.PasswordField(validators=[validators.DataRequired()])

    def validate_login(self, field):
        user = self.get_user()

        if user is None:
            raise validators.ValidationError('Invalid user')

        if not check_password_hash(user.password, self.password.data):
            raise validators.ValidationError('Invalid password')

    def get_user(self):
        return db.session.query(User).filter_by(login=self.login.data).first()


@blueprint.route("/login", methods=["GET", "POST"])
def login():
    form = LoginForm()
    if form.validate_on_submit():
        login_user(form.get_user())
        flash("Logged in successfully.")
        return redirect(request.args.get("next") or url_for("main.index"))
    return render_template("login.html", form=form)


@blueprint.route("/logout")
@login_required
def logout():
    logout_user()
    flash("You have logged out.")
    return redirect(url_for("main.index"))