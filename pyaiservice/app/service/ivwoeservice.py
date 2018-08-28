"""
    create by Fred on 2018/8/22
"""
from flask import current_app

__author__ = 'Fred'

class IvWoEService:
    
    @staticmethod
    def iv_woe(form):
        current_app.logger.debug('iv_woe() called...')    
        try:
            # put you business code here.
            current_app.logger.debug('put you business code here.')
            
        except Exception as e:
            current_app.logger.exception('%r' % e)