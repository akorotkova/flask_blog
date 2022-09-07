from datetime import datetime
from flask import Flask, render_template, url_for, flash, redirect
from flask_sqlalchemy import SQLAlchemy
import config
from .forms import RegistrationForm, LoginForm

app = Flask(__name__)
db = SQLAlchemy(app)
app.config.from_object(config.DevelopmentConfig)


class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(20), unique=True, nullable=False)
    email = db.Column(db.String(120), unique=True, nullable=False)
    password = db.Column(db.String(60), nullable=False)
    image_file = db.Column(db.String(20), nullable=False, default='default.jpg')
    posts = db.relationship('Post', backref='author', lazy=True)

    def __repr__(self):
        return f'(User: name - {self.username}, email - {self.email}, image_file - {self.image_file})'


class Post(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(100), nullable=False)
    date_posted = db.Column(db.DateTime, nullable=False, default=datetime.utcnow)
    content = db.Column(db.Text, nullable=False)
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'), nullable=False)

    def __repr__(self):
        return f'(Post: title - {self.title}, date_posted - {self.date_posted})'


posts = [
    {
        'author': 'Anastasia',
        'title': 'Пост №1', 
        'content': 'Содержание поста №1',
        'date_posted': 'Сентябрь 1, 2022'
    }, 
    {
        'author': 'Maria',
        'title': 'Пост №2', 
        'content': 'Содержание поста №2',
        'date_posted': 'Сентябрь 2, 2022'
    }, 
    {
        'author': 'Alexander',
        'title': 'Пост №3', 
        'content': 'Содержание поста №3',
        'date_posted': 'Сентябрь 3, 2022'
    }, 
    {
        'author': 'Svetlana',
        'title': 'Пост №4', 
        'content': 'Содержание поста №4',
        'date_posted': 'Сентябрь 4, 2022'
    }, 
    {
        'author': 'Dmitry',
        'title': 'Пост №5', 
        'content': 'Содержание поста №5',
        'date_posted': 'Сентябрь 5, 2022'
    }
]


@app.route("/")
@app.route('/index')
def index():
    return render_template('index.html', posts=posts, title='Главная')


@app.route('/about')
def about():
    return render_template('about.html', title='О блогe')


@app.route('/register', methods=['GET', 'POST'])
def register():
    registration_form = RegistrationForm()
    if registration_form.validate_on_submit():
        flash(f'{registration_form.username.data}, Ваша учетная запись создана, добро пожаловать!', 'success')
        return redirect(url_for('index'))
    return render_template('register.html', title='Регистрация', form=registration_form)


@app.route('/login', methods=['GET', 'POST'])
def login():
    login_form = LoginForm()
    if login_form.validate_on_submit():
        if login_form.email.data == 'admin@yandex.ru' and login_form.password.data == '1234567890':
            flash(f'Добро пожаловать!', 'success')
            return redirect(url_for('index'))
        else:
            flash(f'Неверный адрес электронной почты или пароль, повторите попытку', 'danger')
    return render_template('login.html', title='Вход', form=login_form)
