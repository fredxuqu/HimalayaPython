"""
    create by Fred on 2018/8/22
"""
import unittest
from flask_restful import marshal
import json

from app.entity.sampleentity import SampleEntity

__author__ = 'Fred'


class TestCase(unittest.TestCase):

    def setUp(self):
        unittest.TestCase.setUp(self)

    def tearDown(self):
        unittest.TestCase.tearDown(self)

    def test_marshal(self):
        model = SampleEntity("test sample", "2018010110")
        
        # convert object to json 
        json_data = json.dumps(marshal(model, SampleEntity.marshal_fields))
        print(json_data)
        
        # load json object to json string
        json_str = json.loads(json_data)
        print(json_str)
    
            
if __name__ == '__main__':
    unittest.main()
