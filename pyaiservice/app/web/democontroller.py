"""
    create by Fred on 2018/8/22
"""
from flask import current_app
from flask import Blueprint, jsonify, request
from app.service.demoservice import DemoService
from app.forms.demoform import DemoForm
from app.models.demomodel import DemoModel

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
    return 'Py AI Center Service is running...', 200, headers


@democontroller.route('/pyai/demoget', methods=['GET'])
def demoget():
    userid = request.args['userid']
    username = request.args['username']
    print (userid + ' ' + username)
    return "Create user " + username + " success"


@democontroller.route('/pyai/demopost', methods=['GET','POST'])
def demopost():
    try:
        yield
        demoForm = DemoForm(request.form)
        if demoForm.validate():
            username = request.form['username']
            email = request.form['email']
            current_app.logger.debug(username + ' ' + email)
            current_app.logger.debug(demoForm.username.data + ' ' + demoForm.email.data)
            return jsonify({'msg':'Create user ' + username + ' success'})
        else:
            return jsonify({'msg':'Invalid args!'})
    except Exception as e:
        current_app.logger.exception('%r' % e)


@democontroller.route('/pyai/demo/save', methods=['GET','POST'])
def save():
    try:
        demoForm = DemoForm(request.form)
        if demoForm.validate():
            current_app.logger.debug('Create user : ' + demoForm.username.data + ' ' + demoForm.email.data)
            model = DemoModel(demoForm.username.data, demoForm.email.data)
            DemoService.save(model)        
            return jsonify({'msg':'Create user ' + model.username + ' success'})
        else:
            return jsonify({'msg':'Invalid args!'})
    except Exception as e:
        current_app.logger.exception('%r' % e)
        
    
@democontroller.route('/pyai/demo/queryall', methods=['GET','POST'])
def queryall():
    result = DemoService.queryall()
    return jsonify(result)
    
    
@democontroller.route('/pyai/demo/get', methods=['GET','POST'])
def get():
    username = request.args['username']
    result = DemoService.queryByName(username)
    return jsonify(result)


@democontroller.route('/pyai/demo/delete', methods=['GET','POST'])
def delete():
    username = request.args['username']
    result = DemoService.delete(username)
    return jsonify(result)


@democontroller.route('/pyai/demo/<isbn>', methods=['GET','POST'])
def isbn(isbn):
    result = DemoService.isbn(isbn)
    print (result)
    return jsonify(result)


@democontroller.route('/pyai/demo/search', methods=['GET','POST'])
def search():
    keyword = request.form['q']
    page = int(request.form['page'])
    result = DemoService.search(keyword, page)
    return jsonify(result)

