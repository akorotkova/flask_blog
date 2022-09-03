from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SubmitField, BooleanField
from wtforms.validators import DataRequired, Length, Email, EqualTo


class RegistrationForm(FlaskForm):
    username = StringField('Введите имя', 
                            validators=[DataRequired(), Length(min=2, max=20)])
    email = StringField('Введите почту', 
                            validators=[DataRequired(), Email()])
    password = PasswordField('Придумайте пароль', 
                            validators=[DataRequired(), Length(min=8)])
    confirm_password = PasswordField('Подтвердите пароль', 
                            validators=[DataRequired(), EqualTo('password')])
    submit = SubmitField('Отправить')


class LoginForm(FlaskForm):
    email = StringField('Введите почту', 
                            validators=[DataRequired(), Email()])
    password = PasswordField('Введите пароль', 
                            validators=[DataRequired()])
    remember = BooleanField('Запомнить')
    submit = SubmitField('Войти')
