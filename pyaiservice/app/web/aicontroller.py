"""
    create by Fred on 2018/8/22
"""
from flask import current_app
from app.forms.ivwoeform import IVWOEForm
from app.service.ivwoeservice import IvWoEService
from flask import Blueprint, jsonify, request


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
    
