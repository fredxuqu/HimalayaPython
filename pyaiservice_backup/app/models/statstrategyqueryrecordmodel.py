"""
    create by Fred on 2018/8/22
"""
from flask_restful import fields
from sqlalchemy import Column, Integer, String
from app.models.base import db, Base

__author__ = 'Fred'

class StatStrategyRecordModel(Base):
    
    __tablename__ = 'TB_STAT_STRATEGY_RECORD'
    
    id = Column(Integer, primary_key=True)
    model_id = Column(Integer, nullable=False)
    strategy_id = Column(Integer, nullable=False)
    batno = Column(String(14), nullable=False)
    result = Column(String(1), nullable=False)
    score = Column(Integer, nullable=False)

    marshal_fields = {}
    marshal_fields['id'] = fields.Integer(attribute='id')
    marshal_fields['model_id'] = fields.Integer(attribute='model_id')
    marshal_fields['strategy_id'] = fields.Integer(attribute='strategy_id')
    marshal_fields['batno'] = fields.String(attribute='batno')
    marshal_fields['result'] = fields.String(attribute='result')
    marshal_fields['score'] = fields.Integer(attribute='score')
           
    def __init__(self, v_model_id, v_strategy_id, v_batno, v_result, v_score):
        Base.__init__(self)
        self.model_id = v_model_id
        self.strategy_id = v_strategy_id
        self.batno = v_batno
        self.result = v_result
        self.score = v_score

    def __repr__(self):
        return '{"id":%r,"model_id":%r, "strategy_id": %r, "batno": %r, "result": %r, "score": %r}' \
               % (self.id, self.model_id, self.strategy_id, self.batno, self.result, self.score)

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
