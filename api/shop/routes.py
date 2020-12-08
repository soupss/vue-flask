"""
routes.py
- provides the api endpoints, or routes
"""

from flask import Blueprint, jsonify, request, Response, abort
from sqlalchemy.exc import IntegrityError
from .models import db, Article

api = Blueprint('api', __name__)

# get all articles
@api.route('/articles/', methods=['GET'])
def get_articles():
    articles = Article.query.all()
    response = {'articles': [a.to_dict() for a in articles]}
    return jsonify(response)

# article by id
@api.route('/articles/<int:id>/', methods=['GET'])
def get_article_by_id(id):
    article = Article.query.get_or_404(id)
    response = {'article': article.to_dict()}
    return jsonify(response)

# add new article
@api.route('/articles/', methods=['POST'])
def add_article():
    data = request.get_json()
    article = Article(data['title'], data['description'], data['price'])
    db.session.add(article)
    try:
        db.session.commit()
        response = Response('Article created successfully', 201, mimetype='application/json')
    except IntegrityError:
        db.session.rollback()
        response = Response(f'Unable to create article: An article with title:"{article.title}" already exists.', 409)
    return response
