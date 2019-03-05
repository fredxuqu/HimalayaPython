"""
    create by Fred on 2018/8/22
"""
from flask import Flask
from app.models.demomodel import db
from app.repository.pymongo.demomongorepository import mongodb
import logging


__author__ = 'Fred'

def register_blueprints(app):
    from app.web.aicontroller import aicontroller
    from app.web.democontroller import democontroller
    app.register_blueprint(aicontroller)
    app.register_blueprint(democontroller)
    
    
def register_logging(app):    
    handler = logging.FileHandler(app.config['LOGGING_FILE'], encoding='UTF-8')
    handler.setLevel(app.config['LOGGING_LEVEL'])    
    logging_format = logging.Formatter(
                '%(asctime)s - %(levelname)s - %(filename)s - %(funcName)s - %(lineno)s - %(message)s')
    handler.setFormatter(logging_format)
    app.logger.addHandler(handler)
    
    
def register_mongodb(app):
    mongodb.init_app(app, None)
    

def create_app():
    app = Flask(__name__)
    app.config.from_object('app.config.settings')
    app.config.from_object('app.config.secure')
    
    register_blueprints(app)
    
    register_logging(app)
    
    register_mongodb(app)
    
    # init db models
    db.init_app(app)
    
    #db.create_all(app=app)
    with app.app_context():
        db.create_all()
        
    return app

