"""
    create by Fred on 2018/8/22
"""
from flask import Blueprint, jsonify, request
from app.service.demoservice import Demo
from app.forms.demoform import DemoForm



__author__ = 'Fred'


#blueprint
democontroller = Blueprint('democontroller', __name__)


@democontroller.route('/pyai/index', methods=['GET'])
def index():
    headers = {
        'content-type': 'application/json',
        #'content-type': 'text/plain',
        'location': 'http://www.bing.com'
    }
#     response = make_response('Py AI Center Service is running...', 200)
#     response.headers = headers 
#     return response
    return 'Py AI Center Service is running...', 200, headers


@democontroller.route('/pyai/demoget', methods=['GET'])
def demoget():
    userid = request.args['userid']
    username = request.args['username']
    print (userid + ' ' + username)
    return "Create user " + username + " success"


@democontroller.route('/pyai/demopost', methods=['GET','POST'])
def demopost():
    demoForm = DemoForm(request.form)
    if demoForm.validate():
        userid = request.form['userid']
        username = request.form['username']
        print (userid + ' ' + username)
        print (demoForm.userid.data + ' ' + demoForm.username.data)
        return jsonify({'msg':'Create user ' + username + ' success'})
    else:
        return jsonify({'msg':'Invalid args!'})


@democontroller.route('/pyai/demo/save', methods=['GET','POST'])
def save():
    result = Demo.save()
    return jsonify(result)


@democontroller.route('/pyai/demo/<isbn>', methods=['GET','POST'])
def isbn(isbn):
    result = Demo.isbn(isbn)
    return jsonify(result)


@democontroller.route('/pyai/demo/search', methods=['GET','POST'])
def search():
    keyword = request.form['q']
    page = int(request.form['page'])
    result = Demo.search(keyword, page)
    return jsonify(result)
