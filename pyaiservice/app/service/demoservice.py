"""
    create by Fred on 2018/8/22
"""
from flask import current_app

from app.http.http import HTTP
from app.models.demomodel import DemoModel
from app.repository.pymysql.demorepository import DemoRepository


__author__ = 'Fred'

class Demo:
    
    repository = DemoRepository()
    
    
    @classmethod
    def save(cls):
        model1 = DemoModel(title= 'java', 
                           author = 'john',
                           binding = 'b11',
                           publisher = 'csdn',
                           price = 12.0,
                           pages = 340,
                           pubdate = '2018-09-01',
                           isbn = 'ISBN0000001',
                           summary = 'mary@example.com',
                           image = 'mary@example.com.jpg')
        DemoRepository.save(cls, model1)
        return 'succ'
    
    
    @classmethod
    def isbn(cls, isbn):
        DemoRepository.save(DemoModel())
        DemoRepository.query(isbn)
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
