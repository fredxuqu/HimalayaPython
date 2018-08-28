"""
    create by Fred on 2018/8/22
"""
import requests

__author__ = 'Fred'

# scrapy, request + beautiful soap
class HTTP:
    @staticmethod
    def get(url, return_json=True):
        req = requests.get(url)
        if req.status_code != 200:
            return {} if return_json else ''
        return req.json() if return_json else req.text
    
    