"""
app.py
- creates a flask app instance and register the database object
"""

from flask import Flask
from flask_cors import CORS

def create_app(app_name='SHOP_API'):
    app = Flask(app_name)
    cors = CORS(app)
    app.config.from_object('app.config.DevelopmentConfig')
    from app.routes import api
    app.register_blueprint(api, url_prefix="/api")
    from app.models import db
    db.init_app(app)
    with app.app_context():
        db.create_all()
    return app
