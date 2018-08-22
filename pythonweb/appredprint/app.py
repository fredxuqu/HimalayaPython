"""
    create by Fred on 2018/8/22
"""
from flask import Flask

__author__ = 'Fred'

def register_blueprints(app):
#     from app.web.book import book
#     from app.web.user import user
#     app.register_blueprint(book)
#     app.register_blueprint(user)
    from appredprint.web import create_blueprint_v1
    app.register_blueprint(create_blueprint_v1(), url_prefix='v1')

def create_app():
    app = Flask(__name__)
    app.config.from_object('app.config.settings')
    app.config.from_object('app.config.secure')
    
    register_blueprints(app)
    
    return app
