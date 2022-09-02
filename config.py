from os import environ, path
from dotenv import load_dotenv

basedir = path.abspath(path.dirname(__file__))
load_dotenv(path.join(basedir, '.env'))


class Config(object):
    SECRET_KEY = environ.get('SECRET_KEY') or "\x9fE\xd8'f\xc2h\xa9\x91\xb9\xa0DpE\xa54\xa0\x8a\x95^\xa4\xdf\xf7\xbd"
    STATIC_FOLDER = 'static'
    TEMPLATES_FOLDER = 'templates'


class DevelopmentConfig(Config):
    FLASK_ENV = 'development'
    DEBUG = True
    TESTING = True


class ProductionConfig(Config):
    FLASK_ENV = 'production'
    DEBUG = False
    TESTING = False
