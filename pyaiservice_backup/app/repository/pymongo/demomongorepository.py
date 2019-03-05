"""
    create by Fred on 2018/8/22
"""
from app.repository.pymongo.basemongorepository import mongodb
from app.repository.pymongo.basemongorepository import BaseMongoRepository

__author__ = 'Fred'


class DemoRepositoryMongo(BaseMongoRepository):
    
    @classmethod
    def insert(self, model):               
        try:
            mongodb.db.ivwoe.insert({"username":model.username, "email":model.email})
        except AttributeError as ex:
            print ("Error: unable to save data" + ex)
        
        
    @classmethod
    def queryAll(cls):       
        try:
            return mongodb.db.ivwoe.find()
        except:
            print ("Error: unable to fecth data from database")
        return None
        
    