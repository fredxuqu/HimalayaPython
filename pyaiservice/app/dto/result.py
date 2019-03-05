"""
    create by Fred on 2018/12/06
"""
import json
from flask import jsonify

__author__ = 'Fred'


class ReturnMsg:

    def __init__(self, v_code, v_message, v_data):
        self.code = v_code
        self.message = v_message
        self.data = v_data

    def __repr__(self):
        return repr(self.code, self.message, self.data)

    def to_json(self):
        return jsonify(json.loads(json.dumps(self, default=lambda o: o.__dict__, sort_keys=True, indent=4)))
