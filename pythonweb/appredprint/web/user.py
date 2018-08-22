"""
    create by Fred on 2018/8/22
"""
# from flask import Blueprint
from appredprint.libs.redprint import Redprint

__author__ = 'Fred'

#blueprint
# user = Blueprint('user', __name__)
api = Redprint('user')

# /v1/get/user
@api.route('/get')
def get_user():
    return "Fred Xu"

# /v1/get/user
@api.route('/create')
def create_user():
    return "Fred Xu"
