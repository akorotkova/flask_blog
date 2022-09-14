from flask import render_template, url_for, flash, redirect, request
from . import app, db, bcrypt
from .forms import RegistrationForm, LoginForm, UpdateAccountForm
from .models import User, Post
from flask_login import login_user, current_user, logout_user, login_required


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
    if current_user.is_authenticated:
        return redirect(url_for('index'))
    form = RegistrationForm()
    if form.validate_on_submit():
        hashed_password = bcrypt.generate_password_hash(form.password.data).decode('utf-8')
        user = User(username=form.username.data, email=form.email.data, password=hashed_password)
        db.session.add(user)
        db.session.commit()
        flash(f'Ваша учетная запись создана, добро пожаловать!', 'success')
        return redirect(url_for('login'))
    return render_template('register.html', title='Регистрация', form=form)


@app.route('/login', methods=['GET', 'POST'])
def login():
    if current_user.is_authenticated:
        return redirect(url_for('index'))
    form = LoginForm()
    if form.validate_on_submit():
        user = User.query.filter_by(email=form.email.data).first()
        if user and bcrypt.check_password_hash(user.password, form.password.data):
            login_user(user, remember=form.remember.data)
            next_page = request.args.get('next')
            return redirect(next_page) if next_page else redirect(url_for('index'))
        else:
            flash(f'Неверный адрес электронной почты или пароль, повторите попытку', 'danger')
    return render_template('login.html', title='Вход', form=form)


@app.route('/logout')
def logout():
    logout_user()
    return redirect(url_for('index'))


@app.route('/account', methods=['GET', 'POST'])
@login_required
def account():
    form = UpdateAccountForm()
    if form.validate_on_submit():
        current_user.username = form.username.data
        current_user.email = form.email.data
        db.session.commit()
        flash('Ваша учетная запись успешно обновлена', 'success')
        return redirect(url_for('account'))
    elif request.method == 'GET':
        form.username.data = current_user.username
        form.email.data = current_user.email
    image_file = url_for('static', filename='img/' + current_user.image_file)
    return render_template('account.html', title='Личный кабинет', image_file=image_file, form=form)
