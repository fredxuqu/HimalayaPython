"""
    create by Fred on 2018/8/22
"""
from flask import Blueprint, jsonify
from app.service.iv_woe import IV_WOE


__author__ = 'Fred'


#blueprint
aicontroller = Blueprint('aicontroller', __name__)


@aicontroller.route('/pyai/iv_woe', methods=['GET','POST'])
def iv_woe():
    result = IV_WOE.iv_woe()
    return jsonify(result)

