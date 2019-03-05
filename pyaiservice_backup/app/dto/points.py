"""
    create by Fred on 2018/8/22
"""

__author__ = 'Fred'


class XYPoints:
    # fpr is x axis, tpr is y axis
    x = 0   # false positive rate
    y = 0   # true positive rate

    def __init__(self, v_fpr_x, v_tpr_y):
        self.x = v_fpr_x
        self.y = v_tpr_y

    def __repr__(self):
        return repr(self.x, self.y)
