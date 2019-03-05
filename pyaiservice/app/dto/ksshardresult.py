"""
    create by Fred on 2018/12/06
"""

__author__ = 'Fred'


class KSShardResult:

    shard_name = ""
    count_bad = 0
    ratio_bad = 0.00
    count_good = 0
    ratio_good = 0.00
    total_count = 0
    ks_value = 0.00

    def __init__(self, v_shard_name, v_count_bad, v_ratio_bad, v_count_good, v_ratio_good, v_total_count, v_ks_value):
        self.shard_name = v_shard_name
        self.count_bad = v_count_bad
        self.ratio_bad = v_ratio_bad
        self.count_good = v_count_good
        self.ratio_good = v_ratio_good
        self.total_count = v_total_count
        self.ks_value = v_ks_value

    def __repr__(self):
        return repr(self.shard_name, self.count_bad, self.ratio_bad, self.count_good, self.ratio_good, self.total_count,
                    self.ks_value)
