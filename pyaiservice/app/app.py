"""
    create by Fred on 2018/8/22
"""
from flask import Flask
from app.models.demomodel import db

__author__ = 'Fred'

def register_blueprints(app):
    from app.web.aicontroller import aicontroller
    from app.web.democontroller import democontroller
    app.register_blueprint(aicontroller)
    app.register_blueprint(democontroller)

def create_app():
    app = Flask(__name__)
    app.config.from_object('app.config.settings')
    app.config.from_object('app.config.secure')
    
    register_blueprints(app)
    
    # init db models
    db.init_app(app)
    
    #db.create_all(app=app)
    with app.app_context():
        db.create_all()
        
    return app
