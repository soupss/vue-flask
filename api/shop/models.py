from datetime import datetime
from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

class Article(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(60))
    description = db.Column(db.Text)
    price = db.Column(db.Integer)
    created_at = db.Column(db.DateTime, default=datetime.utcnow)

    def to_dict(self):
        return dict(id=self.id,
                    title=self.title,
                    description=self.description,
                    price=self.price,
                    created_at=self.created_at.strftime('%Y-%m-%d %H:%M:%S'))
