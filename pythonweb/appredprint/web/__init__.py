"""
    create by Fred on 2018/8/22
"""
from flask.blueprints import Blueprint
from appredprint.web import user, book

__author__ = 'Fred'

def create_blueprint_v1():
    bp_v1 = Blueprint('v1', __name__)
    
    user.api.register(bp_v1, url_prefix='/user')
    book.api.register(bp_v1, url_prefix='/book')
    return bp_v1