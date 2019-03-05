"""
    create by Fred on 2018/8/22
"""
from flask import current_app
from flask_restful import marshal
from app.utils.http import HTTP
from app.models.demomodel import UserModel
from app.repository.pymysql.demomysqlrepository import DemoMysqlRepository
import json

__author__ = 'Fred'


repository = DemoMysqlRepository()


class DemoMySQLService:
        
    @classmethod
    def save(cls, demo_model):
        repository.save(demo_model)
        return 'succ'

    @classmethod
    def query_by_name(cls, username):
        model = DemoMysqlRepository.query_by_username(username)
        if model is not None:
            return json.loads(json.dumps(marshal(model, UserModel.marshal_fields)))
        return None

    @classmethod
    def delete(cls, username):
        model = DemoMysqlRepository.queryByUserName(username)
        if model is not None:
            return model.delete()
        return None

    @classmethod
    def query_all(cls):
        data = DemoMysqlRepository.query_all()
        result = []
        for d in data:
            result.append(json.loads(json.dumps(marshal(d, UserModel.marshal_fields))))
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

