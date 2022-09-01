from flask import Flask, render_template, url_for
import config

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
