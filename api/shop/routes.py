"""
routes.py
- provides the api endpoints, or routes
"""

from flask import Blueprint, jsonify, request, make_response, abort
from sqlalchemy.exc import IntegrityError
from .models import db, Article

api = Blueprint('api', __name__)

# get all articles
@api.route('/articles/', methods=['GET'])
def get_articles():
    articles = Article.query.all()
    response = {'articles': [a.to_dict() for a in articles]}
    return make_response(jsonify(response), 200)

# get one article
@api.route('/articles/<int:id>/', methods=['GET'])
def get_article(id):
    article = Article.query.get_or_404(id)
    response = {'article': article.to_dict()}
    return make_response(jsonify(response), 200)

# add new article
@api.route('/articles/', methods=['POST'])
def add_article():
    data = request.get_json()
    article = Article(data['title'], data['description'], data['price'], data['category'])
    db.session.add(article)
    try:
        db.session.commit()
        response = make_response('Article created successfully', 201)
    except IntegrityError:
        db.session.rollback()
        response = make_response(f'Unable to create article: An article with title "{article.title}" already exists.', 409)
    return response

# update article
@api.route('/articles/<int:id>/', methods=['PUT'])
def update_article(id):
    newArticle = Article.query.get_or_404(id)
    data = request.get_json()
    newArticle.update(data['title'], data['description'], data['price'], data['category'])
    db.session.add(newArticle)
    db.session.commit()
    response = make_response('Article updated successfully', 200)
    return response

# delete article
@api.route('/articles/<int:id>/', methods=['DELETE'])
def delete_article(id):
    article = Article.query.get_or_404(id)
    db.session.delete(article)
    db.session.commit()
    return make_response(f'Article deleted with id {id}', 200)

#TODO: update_article PUT
#TODO: delete_article POST
