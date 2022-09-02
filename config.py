from os import environ, path
from dotenv import load_dotenv

basedir = path.abspath(path.dirname(__file__))
load_dotenv(path.join(basedir, '.env'))


class Config(object):
    SECRET_KEY = environ.get('SECRET_KEY')
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
