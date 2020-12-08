"""
app.py
- creates a flask app instance and register the database object
"""

from flask import Flask

def create_app(app_name='banana_api'):
    app = Flask(app_name)
    app.config.from_object('banana.config.DevelopmentConfig')
    from banana.routes import api
    app.register_blueprint(api, url_prefix="/api")
    return app
