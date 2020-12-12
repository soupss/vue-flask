from datetime import datetime
from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

class Article(db.Model):
    __tablename__ = 'articles'
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(60), unique=True, nullable=False)
    description = db.Column(db.Text, nullable=False)
    price = db.Column(db.Integer, nullable=False)
    category = db.Column(db.String(30), nullable=True)
    time_created = db.Column(db.DateTime, default=datetime.utcnow, nullable=False)

    def __init__(self, title, description, price, category=None):
        self.title = title
        self.description = description
        self.price = price
        self.category = category

    def __repr__(self):
        return f"<Article('{self.id}', '{self.title}', '{self.description}', '{self.price}', '{self.category}', '{self.time_created}')>"

    def update(self, title, description, price, category=None):
        self.title = title
        self.description = description
        self.price = price
        self.category = category

    def to_dict(self):
        return dict(id=self.id,
                    title=self.title,
                    description=self.description,
                    price=self.price,
                    category=self.category,
                    time_created=self.time_created)
