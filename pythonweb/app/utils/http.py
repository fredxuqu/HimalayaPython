"""
    create by Fred on 2018/8/22
"""
# from urllib import request
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
    
#         if req.status_code == 200:
#             if return_json:
#                 return req.json()
#             else:
#                 return req.text
#         else:
#             if return_json:
#                 return {}
#             else:
#                 return ''