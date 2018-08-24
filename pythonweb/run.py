"""
    create by Fred on 2018/8/22
"""
from app.app import create_app
from app.config import config

__author__ = 'Fred'

app = create_app()

if __name__ == '__main__':
    app.run(config.HOST, config.PORT, config.DEBUG, None)
