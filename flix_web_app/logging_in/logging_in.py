from flask import Blueprint, render_template, redirect, url_for, session

from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SubmitField
from wtforms.validators import DataRequired, Length, ValidationError

from password_validator import PasswordValidator

import flix_web_app.adapters.repository as repo
import flix_web_app.logging_in.services as services

logging_in_blueprint = Blueprint('logging_in_bp', __name__, url_prefix='/logging_in')


@logging_in_blueprint.route('/register', methods=['GET', 'POST'])
def register():
    registerform = RegistrationForm()
    invalid_username = None

    if registerform.validate_on_submit():
        try:
            services.add_user(registerform.username.data, registerform.password.data, repo.repo_instance)

            return redirect(url_for('logging_in_bp.login'))

        except services.NameNotUniqueException:
            invalid_username = 'Username already in use, please try again'

    return render_template(
        'login_page.html', invalid_username=invalid_username, title='Create Account',
        form=registerform, handler_url= url_for('logging_in_bp.register')
    )


@logging_in_blueprint.route('/login', methods=['GET', 'POST'])
def login():
    loginform = LoginForm()
    invalid_username = None
    invalid_password = None

    if loginform.validate_on_submit():
        try:
            user = services.get_user(loginform.username.data, repo.repo_instance)
            services.validate_user(user.user_name, loginform.password.data, repo.repo_instance)
            session.clear()
            session['username'] = user.user_name
            return redirect(url_for('home_bp.home'))

        except services.UnknownUserException:
            invalid_username = 'Username invalid, please try again'

        except services.ValidationException:
            invalid_password = 'Password does not match, please try again'

    return render_template(
        'login_page.html', title='Login',
        invalid_password=invalid_password, invalid_username=invalid_username,
        form=loginform
    )


@logging_in_blueprint.route('/logout')
def logout():
    session.clear()
    return redirect(url_for('home_bp.home'))


class ValidPassword:
    def __init__(self, message=None):
        if not message:
            message = "Password must be at least 6 characters, and contain at least one digit"
            self.message = message

    def __call__(self, form, field):
        schema = PasswordValidator()
        schema \
            .min(6) \
            .has().digits()
        if not schema.validate(field.data):
            raise ValidationError(self.message)


class RegistrationForm(FlaskForm):
    username = StringField('Username',
                           [DataRequired(message='Required field'),
                            Length(min=5, message='Username must be longer than 5 characters')])
    password = PasswordField('Password',
                             [DataRequired(message='Required field'),
                              ValidPassword()])
    submit = SubmitField('Register')


class LoginForm(FlaskForm):
    username = StringField('Username', [DataRequired(message="Required Field")])
    password = PasswordField('Password', [DataRequired(message="Required Field")])
    submit = SubmitField('Login')