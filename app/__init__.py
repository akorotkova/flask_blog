from flask import Flask, render_template, url_for, flash, redirect
import config
from .forms import RegistrationForm, LoginForm

app = Flask(__name__)
app.config.from_object(config.DevelopmentConfig)

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


@app.route('/login')
def login():
    login_form = LoginForm()
    return render_template('login.html', title='Вход', form=login_form)
