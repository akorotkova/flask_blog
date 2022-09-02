from flask import Flask, render_template, url_for
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
    }
]


@app.route("/")
@app.route('/index')
def index():
    return render_template('index.html', posts=posts, title='Главная')

@app.route('/about')
def about():
    return render_template('about.html', title='О блогe')

@app.route('/register')
def register():
    registration_form = RegistrationForm()
    return render_template('register.html', title='Регистрация', form=registration_form)

@app.route('/login')
def login():
    login_form = LoginForm()
    return render_template('login.html', title='Вход', form=login_form)
