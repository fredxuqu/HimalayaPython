"""
    create by Fred on 2018/8/22
"""
from flask_restful import marshal
from app.models.samplerecordmodel import SampleRecordModel
from app.repository.pymysql.samplerecordmysqlrepository import SampleRecordMysqlRepository
import json

__author__ = 'Fred'


repository = SampleRecordMysqlRepository()


class SampleRecordMySQLService:

    @classmethod
    def query_sample_records_by_sample_id(cls, v_sample_id):
        v_model = repository.query_sample_records_by_sample_id(v_sample_id)
        if v_model is not None:
            return json.loads(json.dumps(marshal(v_model, SampleRecordModel.marshal_fields)))
        return None

    @classmethod
    def query_all(cls):
        v_model = repository.query_all()
        if v_model is not None:
            return json.loads(json.dumps(marshal(v_model, SampleRecordModel.marshal_fields)))
        return None
