"""
    create by Fred on 2018/8/22
"""
from flask import Blueprint
from flask import request

__author__ = 'Fred'


#blueprint
user = Blueprint('user', __name__)


@user.route('/user/get', methods=['GET'])
def get_user():
    return "Fred Xu"


@user.route('/user/create', methods=['GET','POST'])
def create_user():
    userid = request.form['userid']
    username = request.form['username']
    print (userid + ' ' + username)
    
    return "Create user " + username + " success"

