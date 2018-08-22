"""
    create by Fred on 2018/8/22
"""
from app.app import create_app

__author__ = 'Fred'

app = create_app()

if __name__ == '__main__':
    app.run('127.0.0.1', 8080, None, None)
