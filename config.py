import os

basedir = os.path.abspath(os.path.dirname(__file__))
DATABASE = os.path.join(basedir, 'app.db')

MAX_CONTENT_LENGTH = 1024 * 1024

UPLOADS_DEFAULT_DEST = os.path.join(basedir, 'upload/')

SQLALCHEMY_DATABASE_URI = 'sqlite:///' + DATABASE

SQLALCHEMY_TRACK_MODIFICATIONS = False

SECRET_KEY = 'you-will-never-guess'

FLASKY_ADMIN = 'root@gmail.com'
