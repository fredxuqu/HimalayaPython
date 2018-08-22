"""
    create by Fred on 2018/8/22
"""
from flask import Blueprint
from flask.globals import request

__author__ = 'Fred'


#blueprint
user = Blueprint('user', __name__)


@user.route('/user/get', methods=['GET'])
def get_user():
    return "Fred Xu"


@user.route('/user/create', methods=['GET','POST'])
def create_user():
    data = request.json
    
    return "Fred Xu"

