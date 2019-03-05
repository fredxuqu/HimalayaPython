"""
    create by Fred on 2018/11/28
"""
from flask_restful import fields
from sqlalchemy import Column, Integer, String
from app.models.base import db, Base

__author__ = 'Fred'

class SampleRecordModel(Base):
    
    __tablename__ = 'TB_SAMPLE_RECORD'
    
    id = Column(Integer, primary_key=True)
    sample_id = Column(Integer, nullable=False)
    batno = Column(String(14), nullable=False)
    result = Column(String(1), nullable=True)

    marshal_fields = {}
    marshal_fields['id'] = fields.Integer(attribute='id')
    marshal_fields['sample_id'] = fields.Integer(attribute='sample_id')
    marshal_fields['batno'] = fields.String(attribute='batno')
    marshal_fields['result'] = fields.String(attribute='result')

    def __init__(self, v_sample_id, v_batno, v_result):
        Base.__init__(self)
        self.sample_id = v_sample_id
        self.batno = v_batno
        self.result = v_result

    def __repr__(self):
        return '{"id":%r,"sample_id":%r, "batno": %r, "result": %r}' \
               % (self.id, self.sample_id, self.batno, self.result)

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
        except Exception as e:
            print("Error: " + e)
        return None
