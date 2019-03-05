"""
    create by Fred on 2018/8/22
"""
import unittest
from flask import Flask
from flask_pymongo import PyMongo
from flask_pymongo import MongoClient

__author__ = 'Fred'

app = Flask(__name__)
app.config["MONGO_URI"] = "mongodb://localhost:27017/pyai"
mongo = PyMongo(app)
client = MongoClient("localhost:27017")
db = client.pyai


class TestCase(unittest.TestCase):


    def setUp(self):
        unittest.TestCase.setUp(self)


    def tearDown(self):
        unittest.TestCase.tearDown(self)


    def testCreateAll(self):
        pass


    def testSaveClient(self):
        db.ivwoe.insert({"name":"save client"})
        
        
    def testSave(self):
        mongo.db.ivwoe.insert({"name":"fred"})
    
    
    def testQueryById(self):
        result = mongo.db.ivwoe.find_one({"name":"fred"})
        print (result['name'])
        print (result)
    
    
    def testDelete(self):
        pass
    
    
    def testUpdate(self):
        pass
    
    
    def testQueryAll(self):
        list = mongo.db.ivwoe.find()
        for elem in list:
            print (elem)
    
                 
if __name__ == '__main__':
    unittest.main()
    
    