"""
    create by Fred on 2018/8/22
"""
import unittest
from flask_restful import marshal
import json

from app.models.demomodel import DemoModel

__author__ = 'Fred'
    

class TestCase(unittest.TestCase):

    def setUp(self):
        unittest.TestCase.setUp(self)

    def tearDown(self):
        unittest.TestCase.tearDown(self)

    def testmarshal(self):
        model = DemoModel(title= 'java', 
                           author = 'john',
                           binding = 'b11',
                           publisher = 'csdn',
                           price = 12.0,
                           pages = 340,
                           pubdate = '2018-09-01', 
                           isbn = '9787501524044',
                           summary = 'mary@example.com',
                           image = 'mary@example.com.jpg')
        
        # convert object to json 
        jsondata = json.dumps(marshal(model, DemoModel.marshal_fields))
        print (jsondata)
        
        # load json object to json string
        jsonStr = json.loads(jsondata)
        print (jsonStr)
    
            
if __name__ == '__main__':
    unittest.main()
