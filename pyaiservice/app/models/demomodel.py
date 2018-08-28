"""
    create by Fred on 2018/8/22
"""
from flask_restful import fields
from sqlalchemy import Column, Integer, String
from app.models.base import db, Base

__author__ = 'Fred'

class DemoModel(Base):
    
    __tablename__='TB_DEMO'
    
    id = Column(Integer, primary_key=True)
    username = Column(String(80), unique=True, nullable=False)
    email = Column(String(120), unique=True, nullable=False)

    marshal_fields = {}
    marshal_fields['id'] = fields.Integer(attribute='id')
    marshal_fields['username'] = fields.String(attribute='username')
    marshal_fields['email'] = fields.String(attribute='email')
     
     
#     def __init__(self):
#         Base.__init__(self)
         
           
    def __init__(self, v_username, v_email):
        Base.__init__(self)
        self.username = v_username
        self.email = v_email


    def __repr__(self):
        return '<User %r>' % self.username   
    
    
    def save(self):
        try:
            db.session.add(self)
            db.session.commit()
        except:
            return False
        return True
        
        
    def delete(self):
        try:
            db.session.delete(self)
            db.session.commit()
        except:
            return False
        return True
    
    
    def get(self):
        try:
            return db.session.get(self.id)
        except:
            return None
                    