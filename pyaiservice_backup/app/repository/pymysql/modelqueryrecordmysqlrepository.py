"""
    create by Fred on 2018/8/22
"""
from app.models.modelqueryrecordmodel import ModelQueryRecordModel

__author__ = 'Fred'


class ModelQueryRecordMysqlRepository:
    
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
            return ModelQueryRecordModel.query.all()
        except Exception as ex:
            print("Error: " + ex)
        return None

    @classmethod
    def query_model_query_records_by_model_id(cls, v_model_id):
        try:
            return ModelQueryRecordModel.query.filter_by(model_id=v_model_id).first();
        except Exception as ex:
            print("Error: " + ex)
        return None
