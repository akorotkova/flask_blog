from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SubmitField, BooleanField, ValidationError
from wtforms.validators import DataRequired, Length, Email, EqualTo
from .models import User


class RegistrationForm(FlaskForm):
    username = StringField('Введите имя', 
                            validators=[DataRequired(), Length(min=2, max=20)])
    email = StringField('Введите почту', 
                            validators=[DataRequired(), Email(message='Неверный формат электронной почты')])
    password = PasswordField('Придумайте пароль', 
                            validators=[DataRequired(), Length(min=8)])
    confirm_password = PasswordField('Подтвердите пароль', 
                            validators=[DataRequired(), EqualTo('password', message='Пароли не совпадают')])
    submit = SubmitField('Отправить')

    def validate_username(self, username):
        user = User.query.filter_by(username=username.data).first()
        if user:
            raise ValidationError('Данное имя уже занято. Пожалуйста, укажите другое имя')

    def validate_email(self, email):
        user = User.query.filter_by(email=email.data).first()
        if user:
            raise ValidationError('Данный адрес электронной почты уже зарегистрирован. Пожалуйста, укажите другой email')
        


class LoginForm(FlaskForm):
    email = StringField('Введите почту', 
                            validators=[DataRequired(), Email()])
    password = PasswordField('Введите пароль', 
                            validators=[DataRequired()])
    remember = BooleanField('Запомнить')
    submit = SubmitField('Войти')
