from os import environ, path
from dotenv import load_dotenv

class Config:

    FLASK_APP = environ.get('FLASK_APP')
    FLASK_ENV = environ.get('FLASK_ENV')
    SECRET_KEY = environ.get('SECRET_KEY')

    STATIC_FOLDER = 'static'
    TEMPLATES_FOLDER = 'templates'
