"""
    create by Fred on 2018/12/06
"""
import json
from flask import jsonify

__author__ = 'Fred'


class KSResult:

    sample_id = ""
    sample_name = ""
    ks_shards = []
    ks_value = 0.00
    total = 0
    total_good = 0
    total_bad = 0

    def __init__(self, v_sample_id, v_sample_name, v_ks_shards, v_ks_value, v_total, v_total_good, v_total_bad):
        self.sample_id = v_sample_id
        self.sample_name = v_sample_name
        self.ks_shards = v_ks_shards
        self.ks_value = v_ks_value
        self.total = v_total
        self.total_good = v_total_good
        self.total_bad = v_total_bad

    def __repr__(self):
        return repr(self.sample_id, self.sample_name, self.ks_shards, self.ks_value, self.total, self.total_good,
                    self.total_bad)

    def to_json(self):
        return jsonify(json.loads(json.dumps(self, default=lambda o: o.__dict__, sort_keys=True, indent=4)))
