"""
    create by Fred on 2018/8/22
"""
# from flask import Blueprint
from appredprint.libs.redprint import Redprint

__author__ = 'Fred'

#blueprint
# book = Blueprint('book', __name__)
api = Redprint('book')

@api.route('/get')
def get_book():
    return get()
            
def get():
    return "Machine Learing Definition Guide"
