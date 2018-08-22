"""
    create by Fred on 2018/8/22
"""
from flask import Blueprint

__author__ = 'Fred'

#blueprint
book = Blueprint('book', __name__)

@book.route('/book/get', methods=['GET'])
def get_book():
    return get()
            
def get():
    return "Machine Learing Definition Guide"
