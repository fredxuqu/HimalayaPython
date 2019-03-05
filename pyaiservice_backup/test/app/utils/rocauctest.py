"""
    create by Fred on 2018/8/22
"""
import unittest
import numpy as np
from sklearn.metrics import roc_auc_score
from sklearn.metrics import roc_curve

__author__ = 'Fred'
    

class TestCase(unittest.TestCase):

    def setUp(self):
        unittest.TestCase.setUp(self)

    def tearDown(self):
        unittest.TestCase.tearDown(self)

    def testroc(self):
        y_true = np.array([0, 0, 1, 1])
        y_scores = np.array([0.1, 0.4, 0.35, 0.8])
        print(y_true)
        print(y_scores)
        print(len(y_true))
        print(len(y_scores))
        fpr, tpr, _ = roc_curve(y_true, y_scores, None, None, None)
        print(len(fpr))
        print(tpr)
        print(len(tpr))
        print(tpr)

        area = roc_auc_score(y_true, y_scores)
        print(area)


if __name__ == '__main__':
    unittest.main()
