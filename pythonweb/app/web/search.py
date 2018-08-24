# http://t.yushu.im/v2/book/isbn/9787501524044
"""
    create by Fred on 2018/8/22
"""
from app.utils.http import HTTP

__author__ = 'Fred'

class Search:
    isbn_url = 'http://t.yushu.im/v2/book/isbn/{}'
    keyword_url = 'http://t.yushu.im/v2/book/search?q={}&count={}&start={}'
    @classmethod
    def search_by_isbn(cls, isbn):
        url = cls.isbn_url.format(isbn)
        result = HTTP.get(url)
        return result
    
    
    @classmethod
    def search_by_keyword(cls, keyword, count=10, start=0):
        url = cls.keyword_url.format(keyword, count, start)
        result = HTTP.get(url)
        return result
