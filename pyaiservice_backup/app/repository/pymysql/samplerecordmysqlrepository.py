"""
    create by Fred on 2018/8/22
"""
from app.models.samplerecordmodel import SampleRecordModel

__author__ = 'Fred'


class SampleRecordMysqlRepository:

    @classmethod
    def save(cls, sample_model):
        try:
            sample_model.save()
        except Exception as ex:
            print("Error: " + ex)

    @classmethod
    def query_all(cls):
        try:
            return SampleRecordModel.query.all()
        except Exception as ex:
            print("Error: " + ex)
        return None

    @classmethod
    def query_sample_records_by_sample_id(cls, v_sample_id):
        try:
            query = SampleRecordModel.query.filter_by(sample_id=v_sample_id)
            return query.all()
        except Exception as ex:
            print("Error: " + ex)
        return None

    @classmethod
    def query_sample_records_by_sample_id(cls, v_sample_id):
        try:
            query = SampleRecordModel.query.filter_by(sample_id=v_sample_id)
            return query.all()
        except Exception as ex:
            print("Error: " + ex)
        return None
