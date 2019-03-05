"""
    create by Fred on 2018/8/22
"""
from app.entity.modelqueryrecordentity import ModelQueryRecordEntity

__author__ = 'Fred'


class ModelQueryRecordRepository:
    
    @classmethod
    def save(cls, sample_model):
        try:
            sample_model.save()
        except Exception as ex:
            # rollback in case there is any error
            print("Error: " + ex)
            sample_model.session.rollback()

    @classmethod
    def query_all(cls):
        try:
            return ModelQueryRecordEntity.query.all()
        except Exception as ex:
            print("Error: " + ex)
        return None

    @classmethod
    def query_model_query_records_by_model_id(cls, v_model_id):
        try:
            return ModelQueryRecordEntity.query.filter_by(model_id=v_model_id).first();
        except Exception as ex:
            print("Error: " + ex)
        return None
