"""
    create by Fred on 2018/8/22
"""
import unittest
from flask import Flask
from flask.globals import current_app

__author__ = 'Fred'

app = Flask(__name__)

with app.app_context():
    currentApp = current_app
    print (current_app.config['DEBUG'])
    

class TestCase(unittest.TestCase):

    def setUp(self):
        unittest.TestCase.setUp(self)

    def tearDown(self):
        unittest.TestCase.tearDown(self)

    def testMet1(self):
        print ('===========================')
        print ('Debug value : ' + currentApp.config['DEBUG'])
        pass
    
    def testException(self):
        try:
            f=open(r'd:\t.txt')
            print(f.read())
        finally:
            f.close()
            
    def testWith(self):
        with open(r'd:\t.txt') as f:
            print(f.read())

            
if __name__ == '__main__':
    unittest.main()
