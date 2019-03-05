"""
    create by Fred on 2018/8/22
"""
from flask import current_app
from app.forms.ivwoeform import IVWOEForm
from app.service.ivwoeservice import IvWoEService
from flask_restful import marshal
import json
from flask import Blueprint, jsonify, request
from app.dto.result import ReturnMsg
from app.service.rocauccalculateservice import ROCAUCCalculateService
from app.service.kscalculateservice import KSCalculateService


__author__ = 'Fred'


#blueprint
aicontroller = Blueprint('aicontroller', __name__)


@aicontroller.route('/pyai/iv_woe', methods=['GET','POST'])
def iv_woe():
    current_app.logger.debug('Enter...')    
    try:
        ivwoeForm = IVWOEForm(request.form)
        if ivwoeForm.validate():
            
            # logging args as info
            current_app.logger.info('logging args as info')
            
            IvWoEService.iv_woe(ivwoeForm)
            
            current_app.logger.info('ivwoe called success')
            
            return "succ"
        else:
            current_app.logger.warning('args are invalid')
            
    except Exception as e:
        current_app.logger.exception('%r' % e)


@aicontroller.route('/pyai/cal_roc_auc', methods=['GET'])
def cal_roc_auc():
    current_app.logger.debug('Enter ROC and AUC Calculating Service ...')
    try:
        model_id = request.args['model_id']
        strategy_id = request.args['strategy_id']
        sample_ids = request.args['sample_ids']

        if model_id is None:
            return default_error_message("模型ID为空")
        if sample_ids is None:
            return default_error_message("样本ID不能为空")

        result = ROCAUCCalculateService.cal_roc_auc(sample_ids, model_id, strategy_id)
        return_msg = ReturnMsg("0", "ROC & AUC 计算成功", result)
        return return_msg.to_json()
    except Exception as e:
        current_app.logger.exception('%r' % e)
        return default_error_message()


@aicontroller.route('/pyai/cal_ks', methods=['GET'])
def cal_ks():
    current_app.logger.debug('Enter ROC and AUC Calculating Service ...')
    try:
        model_id = request.args['model_id']
        strategy_id = request.args['strategy_id']
        sample_ids = request.args['sample_ids']

        if model_id is None:
            return default_error_message("模型ID为空")
        if sample_ids is None:
            return default_error_message("样本ID不能为空")

        result = KSCalculateService.cal_ks(sample_ids, model_id, strategy_id)
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
