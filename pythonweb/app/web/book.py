"""
    create by Fred on 2018/8/22
"""
from flask import Blueprint, jsonify
from app.web.search import Search

__author__ = 'Fred'


#blueprint
book = Blueprint('book', __name__)


@book.route('/book/get', methods=['GET'])
def get_book():
    return get()


@book.route('/book/searchisbn/<q>', methods=['GET'])
def searchbyisbn(q):
    result = Search.search_by_isbn(q)
    return jsonify(result)
   
   
@book.route('/book/searchbykey/<q>/<page>', methods=['GET'])
def searchbykey(q, page):
    result = Search.search_by_keyword(q, 10, 0)
    return jsonify(result)
        
            
def get():
    return "Machine Learing Definition Guide"

