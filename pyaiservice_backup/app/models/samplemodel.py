"""
    create by Fred on 2018/11/28
"""
from flask_restful import fields
from sqlalchemy import Column, Integer, String
from app.models.base import db, Base

__author__ = 'Fred'


class SampleModel(Base):
    
    __tablename__ = 'TB_SAMPLE'
    
    id = Column(Integer, primary_key=True)
    name = Column(String(28), nullable=False)
    batno = Column(String(14), nullable=False)

    marshal_fields = {}
    marshal_fields['id'] = fields.Integer(attribute='id')
    marshal_fields['name'] = fields.String(attribute='name')
    marshal_fields['batno'] = fields.String(attribute='batno')

    def __init__(self, v_name, v_batno):
        Base.__init__(self)
        self.name = v_name
        self.batno = v_batno

    def __repr__(self):
        return '{"id":%r,"name":%r, "batno": %r}' % (self.id, self.name, self.batno)

    def save(self):
        try:
            db.session.add(self)
            db.session.commit()
        except Exception as e:
            print("Error: " + e)
            db.session.rollback()
            return False
        return True

    def delete(self):
        try:
            db.session.delete(self)
            db.session.commit()
        except Exception as e:
            print("Error: " + e)
            db.session.rollback()
            return False
        return True

    def get(self):
        try:
            return db.session.get(self.id)
        except:
            return None
