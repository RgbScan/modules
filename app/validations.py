from wtforms import StringField, PasswordField, SubmitField, BooleanField
from flask_wtf import FlaskForm
from wtforms.validators import DataRequired, Email, EqualTo, Length
from email_validator import validate_email, EmailNotValidError


class RegistrationForm(FlaskForm):
    login = StringField('Логин', validators=[DataRequired(), Length(min=3, max=25)])
    email = StringField('Email', validators=[DataRequired(), Email()])
    password = PasswordField('Пароль', validators=[DataRequired(), Length(min=6)])
    confirm_password = PasswordField('Подтверждение пароля', validators=[DataRequired(), EqualTo('password')])
    submit = SubmitField('Создать аккаунт')


class LoginForm(FlaskForm):
    login = StringField('Логин', validators=[DataRequired()])
    password = PasswordField('Пароль', validators=[DataRequired()])
    remember_me = BooleanField('Запомнить меня')
    submit = SubmitField('Войти')