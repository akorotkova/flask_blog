import logging
from logging.handlers import SMTPHandler
from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_bcrypt import Bcrypt
from flask_login import LoginManager
from config import Config


db = SQLAlchemy()
flask_bcrypt = Bcrypt()
login_manager = LoginManager()
login_manager.login_view = 'users.login'
login_manager.login_message = 'Пожалуйста, войдите в систему, чтобы получить доступ к странице'
login_manager.login_message_category = 'info'


def create_app(config_class=Config):

    app = Flask(__name__)
    app.config.from_object(config_class)

    db.init_app(app)
    flask_bcrypt.init_app(app)
    login_manager.init_app(app)

    from .users import users
    from .posts import posts
    from .main import main
    from .errors import errors
    app.register_blueprint(users)
    app.register_blueprint(posts)
    app.register_blueprint(main)
    app.register_blueprint(errors)
    
    if not app.config['DEBUG'] and not app.config['TESTING']:

        mail_handler = SMTPHandler(
                mailhost=(app.config['MAIL_SERVER'], app.config['MAIL_PORT']),
                fromaddr=app.config['MAIL_USERNAME'],
                toaddrs=app.config['MAIL_USERNAME'], subject='Application Error',
                credentials=(app.config['MAIL_USERNAME'], app.config['MAIL_PASSWORD']), secure=())
        mail_handler.setLevel(logging.ERROR)
        app.logger.addHandler(mail_handler)

    return app
