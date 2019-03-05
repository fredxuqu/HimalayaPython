"""
    create by Fred on 2018/8/22
"""
from flask import current_app
from flask import Blueprint, jsonify, request
from app.service.demomysqlservice import DemoMySQLService
from app.service.samplemysqlservice import SampleMySQLService
from app.service.samplerecordmysqlservice import SampleRecordMySQLService
from app.service.modelqueryrecordmysqlservice import ModelQueryRecordMySQLService
from app.service.statstrategyqueryrecordmysqlservice import StrategyQueryRecordMySQLService
from app.forms.demoform import DemoForm
from app.models.demomodel import UserModel
from app.service.demomongoservice import DemoMongoService
from app.dto.rocaucresult import RocAucResult
from flask_restful import marshal
import json
from app.dto.result import ReturnMsg

__author__ = 'Fred'

#blueprint
democontroller = Blueprint('democontroller', __name__)

@democontroller.route('/pyai/index', methods=['GET'])
def index():
    headers = {
        'content-type': 'application/json',
        'location': 'http://www.bing.com'
    }
    return 'Py AI Center Service is running...', 200, headers


@democontroller.route('/pyai/sample/queryall', methods=['GET', 'POST'])
def query_all_sample():
    result = SampleMySQLService.query_all()
    return jsonify(result)


@democontroller.route('/pyai/sample/getbyid', methods=['GET', 'POST'])
def get_by_sample_id():
    sample_id = request.args['sample_id']
    result = SampleMySQLService.query_by_sample_id(sample_id)
    return jsonify(result)


@democontroller.route('/pyai/samplerecord/queryall', methods=['GET', 'POST'])
def sample_record_query_all():
    result = SampleRecordMySQLService.query_all()
    return jsonify(result)


@democontroller.route('/pyai/samplerecord/getbymodelid', methods=['GET', 'POST'])
def get_sample_by_model_id():
    sample_id = request.args['sample_id']
    result = SampleRecordMySQLService.query_sample_records_by_sample_id(sample_id)
    return jsonify(result)


@democontroller.route('/pyai/modelquery/queryall', methods=['GET', 'POST'])
def model_query_record_query_all():
    result = ModelQueryRecordMySQLService.query_all()
    return jsonify(result)


@democontroller.route('/pyai/modelquery/getrecordbymodelid', methods=['GET', 'POST'])
def get_model_query_records_by_model_id():
    model_id = request.args['model_id']
    result = ModelQueryRecordMySQLService.query_model_query_records_by_model_id(model_id)
    return jsonify(result)


@democontroller.route('/pyai/strategyquery/queryall', methods=['GET', 'POST'])
def strategy_query_record_query_all():
    result = StrategyQueryRecordMySQLService.query_all()
    return jsonify(result)


@democontroller.route('/pyai/strategyquery/getrecordbystrategyid', methods=['GET', 'POST'])
def get_strategy_query_records_by_strategy_id():
    strategy_id = request.args['strategy_id']
    result = StrategyQueryRecordMySQLService.query_strategy_query_records_by_model_id(strategy_id)
    return jsonify(result)


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


@democontroller.route('/pyai/demo/savemongo', methods=['GET','POST'])
def save_mongo():
    try:
        demoForm = DemoForm(request.form)
        if demoForm.validate():
            current_app.logger.debug('Create user : ' + demoForm.username.data + ' ' + demoForm.email.data)
            model = UserModel(demoForm.username.data, demoForm.email.data)
            DemoMongoService.save_mongo(model)
            return jsonify({'msg':'Create user ' + model.username + ' success'})
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
            model = UserModel(demoForm.username.data, demoForm.email.data)
            DemoMySQLService.save(model)
            return jsonify({'msg':'Create user ' + model.username + ' success'})
        else:
            return jsonify({'msg':'Invalid args!'})
    except Exception as e:
        current_app.logger.exception('%r' % e)
        
    
@democontroller.route('/pyai/demo/queryall', methods=['GET','POST'])
def queryall():
    result = DemoMySQLService.query_all()
    return jsonify(result)
    
    
@democontroller.route('/pyai/demo/get', methods=['GET','POST'])
def get():
    username = request.args['username']
    result = DemoMySQLService.query_by_name(username)
    return jsonify(result)


@democontroller.route('/pyai/demo/delete', methods=['GET','POST'])
def delete():
    username = request.args['username']
    result = DemoMySQLService.delete(username)
    return jsonify(result)


@democontroller.route('/pyai/demo/<isbn>', methods=['GET','POST'])
def isbn(isbn):
    result = DemoMySQLService.isbn(isbn)
    print (result)
    return jsonify(result)


@democontroller.route('/pyai/demo/search', methods=['GET','POST'])
def search():
    keyword = request.form['q']
    page = int(request.form['page'])
    result = DemoMySQLService.search(keyword, page)
    return jsonify(result)


@democontroller.route('/pyai/demo/error', methods=['GET','POST'])
def error():
    error_result = ReturnMsg("-1", "Error", None)
    result = json.loads(json.dumps(error_result, default=lambda o: o.__dict__, sort_keys=True, indent=4))
    return jsonify(result)


@democontroller.route('/pyai/demo/succ', methods=['GET','POST'])
def succ():
    rocauc = RocAucResult("1", "2", None, None)
    succ_result = ReturnMsg("0", "Success", rocauc)
    result = json.loads(json.dumps(succ_result, default=lambda o: o.__dict__, sort_keys=True, indent=4))
    return jsonify(result)


@democontroller.route('/pyai/demo/tt', methods=['GET','POST'])
def tt():
    rocauc = RocAucResult("1", "2", None, None)
    result = json.loads(json.dumps(rocauc, default=lambda o: o.__dict__, sort_keys=True, indent=4))
    # return json.loads(json.dumps(marshal(succ_result, ReturnMsg.marshal_fields)))
    return jsonify(result)