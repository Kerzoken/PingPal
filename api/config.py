import os

SECRET_KEY = os.urandom(32)

basedir = os.path.abspath(os.path.dirname(__file__))

DEBUG = True
print("DATABASE_URL:", os.getenv('DATABASE_URL'))
SQLALCHEMY_DATABASE_URI = os.getenv(
    'DATABASE_URL') or 'sqlite:///' + os.path.join(basedir, 'app.db')
SQLALCHEMY_TRACK_MODIFICATIONS = False
