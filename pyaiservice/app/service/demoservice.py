"""
    create by Fred on 2018/8/22
"""
from flask import current_app
from flask_restful import marshal
from app.utils.http import HTTP
from app.models.demomodel import DemoModel
from app.repository.pymysql.demorepository import DemoRepository
import json

__author__ = 'Fred'


repository = DemoRepository()


class DemoService:
        
    @classmethod
    def save(cls, demomodel):
        repository.save(demomodel);
        return 'succ'
        
        
    @classmethod
    def queryByName(cls, username):
        model = DemoRepository.queryByUserName(username)
        if model != None:
            return json.loads(json.dumps(marshal(model, DemoModel.marshal_fields)))
        return None
    
    
    @classmethod
    def delete(cls, username):
        model = DemoRepository.queryByUserName(username)
        if model != None:
            return model.delete()
        return None
        
        
    @classmethod
    def queryall(cls):
        data = DemoRepository.queryAll() 
        result = []
        for d in data:
            result.append(json.loads(json.dumps(marshal(d, DemoModel.marshal_fields))))
        return result
        
        
    @classmethod
    def isbn(cls, isbn):
        isbn_url = 'http://t.yushu.im/v2/book/isbn/{}'
        url = isbn_url.format(isbn)
        result = HTTP.get(url)
        return result
    
    
    @classmethod
    def search(cls, keyword, page):
        url = 'http://t.yushu.im/v2/book/search?q={}&count={}&start={}'
        url = url.format(keyword, 
                         current_app.config['PAGE_SIZE'], 
                         cls.compute_start(page))
        result = HTTP.get(url)
        return result
        
        
    @classmethod
    def compute_start(cls, page):
        return (page-1) * current_app.config['PAGE_SIZE']

