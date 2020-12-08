"""
app.py
- creates a flask app instance and register the database object
"""

from flask import Flask

def create_app(app_name='SHOP_API'):
    app = Flask(app_name)
    app.config.from_object('shop.config.DevelopmentConfig')
    from shop.routes import api
    app.register_blueprint(api, url_prefix="/api")
    return app
