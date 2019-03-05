"""
    create by Fred on 2018/8/22
"""

__author__ = 'Fred'


class RocAucResult:
    sample_id = ""
    sample_name = ""
    roc = []
    auc = 0.0

    def __init__(self, v_sample_id, v_sample_name, v_roc_points, v_auc_value):
        self.sample_id = v_sample_id
        self.sample_name = v_sample_name
        self.roc = v_roc_points
        self.auc = v_auc_value

    def __repr__(self):
        return repr(self.sample_id, self.sample_name, self.roc, self.auc)
