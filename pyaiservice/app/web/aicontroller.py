"""
    create by Fred on 2018/8/22
"""
from flask import current_app
from app.service.ivwoeservice import IvWoEService
import json
from flask import Blueprint, request
from app.dto.result import ReturnMsg
from app.service.rocauccalculateservice import ROCAUCCalculateService
from app.service.kscalculateservice import KSCalculateService


__author__ = 'Fred'


# blueprint
aicontroller = Blueprint('aicontroller', __name__)


@aicontroller.route('/pyai/index', methods=['GET', "POST"])
def index():
    headers = {
        'content-type': 'application/json',
        'location': 'http://www.bing.com'
    }
    return 'Py AI Center Service is running...', 200, headers


"""
@aicontroller.route('/pyai/getpost', methods=['GET', "POST"])
def get():
    foo = request.args["foo"]
    print(foo)
    headers = {
        'content-type': 'application/json',
        'location': 'http://www.bing.com'
    }
    return 'Get method called, args : ' + foo, 200, headers


@aicontroller.route('/pyai/post_form', methods=['POST'])
def post_form():
    foo = request.form["foo"]
    print(foo)
    headers = {
        'content-type': 'application/json',
        'location': 'http://www.bing.com'
    }
    return 'Get request parameter from form ' + foo, 200, headers

# Content-Type should be application/json
# parameter should be formatted json
# {
#  "model_id":"10",
#  "sample_ids":"20",
#  "strategy_id":""
# }
@aicontroller.route('/pyai/req_json', methods=['POST'])
def req_json():
    params = request.get_json()
    print(params["foo"])
    json_str = json.dumps(params, default=lambda o: o.__dict__, sort_keys=True, indent=4)
    print(json_str)
    headers = {
        'content-type': 'application/json',
        'location': 'http://www.bing.com'
    }
    return 'Get request parameter from json ' + json_str, 200, headers
"""


@aicontroller.route('/pyai/iv_woe', methods=['POST'])
def iv_woe():
    current_app.logger.debug('Enter...')
    try:
        params = request.get_json()
        print(params["foo"])
        json_str = json.dumps(params, default=lambda o: o.__dict__, sort_keys=True, indent=4)
        print(json_str)
        headers = {
            'content-type': 'application/json',
            'location': 'http://www.bing.com'
        }
        return 'Get request parameter from json ' + json_str, 200, headers
    except Exception as e:
        current_app.logger.exception('%r' % e)


@aicontroller.route('/pyai/cal_roc_auc', methods=['POST'])
def cal_roc_auc():
    current_app.logger.debug('Enter ROC and AUC Calculating Service ...')
    try:
        params = request.get_json()
        model_id = params["model_id"]
        strategy_id = params["strategy_id"]
        sample_ids = str(params["sample_ids"])

        if model_id is None and len(model_id) <= 0:
            return default_error_message("模型ID为空")

        if sample_ids is None and len(model_id) <= 0:
            return default_error_message("样本ID不能为空")

        if strategy_id is not None and len(strategy_id) > 0:
            strategy_id = int(strategy_id)

        result = ROCAUCCalculateService.cal_roc_auc(sample_ids, int(model_id), strategy_id)
        return_msg = ReturnMsg("0", "ROC & AUC 计算成功", result)
        return return_msg.to_json()
    except Exception as e:
        current_app.logger.exception('%r' % e)
        return default_error_message()


@aicontroller.route('/pyai/cal_ks', methods=['POST'])
def cal_ks():
    current_app.logger.debug('Enter ROC and AUC Calculating Service ...')
    try:
        params = request.get_json()
        model_id = params["model_id"]
        strategy_id = params["strategy_id"]
        sample_ids = str(params["sample_ids"])

        if model_id is None and len(model_id) <= 0:
            return default_error_message("模型ID为空")

        if sample_ids is None and len(model_id) <= 0:
            return default_error_message("样本ID不能为空")

        if strategy_id is not None and len(strategy_id) > 0:
            strategy_id = int(strategy_id)

        result = KSCalculateService.cal_ks(sample_ids, int(model_id), strategy_id)
        return_msg = ReturnMsg("0", "KS计算成功", result)
        return return_msg.to_json()
    except Exception as e:
        current_app.logger.exception('%r' % e)
        return default_error_message()


@classmethod
def default_error_message(cls, v_message):
    if v_message is None or len(v_message) <= 0:
        v_message = "ROC and AUC calculate failed!"
    return_msg = ReturnMsg("-1", v_message, None)
    return return_msg.to_json()
