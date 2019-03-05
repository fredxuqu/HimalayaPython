"""
    create by Fred on 2018/12/06
"""

__author__ = 'Fred'


class KSShardRule:
    shard_name = None
    score_start = 0
    score_end = 0

    def __init__(self, v_shard_name, v_score_start, v_score_end):
        self.shard_name = v_shard_name
        self.score_start = v_score_start
        self.score_end = v_score_end

    def __repr__(self):
        return repr(self.shard_name, self.score_start, self.score_end)
