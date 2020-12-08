"""
config.py
- settings for the flask application object
"""

class Config():
    DEBUG = False
    SQLALCHEMY_DATABASE_URI = 'sqlite:///shop.db'
    SQLALCHEMY_TRACK_MODIFICATION = False
    SECRET_KEY = 'mysecretkey'

class DevelopmentConfig(Config):
    ENV = 'development'
    DEBUG = True
