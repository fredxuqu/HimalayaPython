"""
    create by Fred on 2018/8/22
"""
from flask_restful import marshal
from app.utils.http import HTTP
from app.models.demomodel import DemoModel
from app.repository.pymongo.demomongorepository import DemoRepositoryMongo
import json

__author__ = 'Fred'


repository_mongo = DemoRepositoryMongo()

class DemoMongoService:
    
    @classmethod
    def savemongo(cls, demomodel):
        jsonstr = json.dumps(marshal(demomodel, DemoModel.marshal_fields))
        repository_mongo.insert(demomodel);
        return 'succ'