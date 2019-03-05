"""
    create by Fred on 2018/8/22
"""
from flask_restful import marshal
from app.models.demomodel import UserModel
from app.repository.pymongo.demomongorepository import DemoRepositoryMongo
import json

__author__ = 'Fred'


repository_mongo = DemoRepositoryMongo()


class DemoMongoService:
    
    @classmethod
    def save_mongo(cls, demomodel):
        json_str = json.dumps(marshal(demomodel, UserModel.marshal_fields))
        print(json_str)
        repository_mongo.insert(demomodel);
        return True