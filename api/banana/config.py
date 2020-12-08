"""
config.py
- settings for the flask application object
"""

class Config():
    DEBUG = False
    SQLALCHEMY_DATABASE_URI = 'sqlite:///banana.db'
    SQLALCHEMY_TRACK_MODIFICATION = False
    SECRET_KEY = 'mysecretkey'

class DevelopmentConfig(Config):
    DEBUG = True
