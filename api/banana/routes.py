"""
routes.py
- provides the api endpoints, or routes
"""

from flask import Blueprint, jsonify, request

api = Blueprint('api', __name__)

@api.route('/banana')
def read():
    response = { 'success': True }
    return jsonify(response)
