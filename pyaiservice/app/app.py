"""
    create by Fred on 2018/8/22
"""
from flask import Flask
from app.entity.sampleentity import db
import logging


__author__ = 'Fred'


def register_blueprints(app):
    from app.web.aicontroller import aicontroller
    app.register_blueprint(aicontroller)
    
    
def register_logging(app):    
    handler = logging.FileHandler(app.config['LOGGING_FILE'], encoding='UTF-8')
    handler.setLevel(app.config['LOGGING_LEVEL'])    
    logging_format = logging.Formatter(
                '%(asctime)s - %(levelname)s - %(filename)s - %(funcName)s - %(lineno)s - %(message)s')
    handler.setFormatter(logging_format)
    app.logger.addHandler(handler)


def create_app():
    app = Flask(__name__)
    app.config.from_object('app.config.settings')
    app.config.from_object('app.config.secure')
    
    register_blueprints(app)
    
    register_logging(app)

    # init db models
    db.init_app(app)
    
    # db.create_all(app=app)
    with app.app_context():
        db.create_all()
        
    return app

