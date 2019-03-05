"""
    create by Fred on 2018/8/22
"""
from flask_restful import marshal
from app.models.modelqueryrecordmodel import ModelQueryRecordModel
from app.repository.pymysql.modelqueryrecordmysqlrepository import ModelQueryRecordMysqlRepository
import json

__author__ = 'Fred'


repository = ModelQueryRecordMysqlRepository()


class ModelQueryRecordMySQLService:

    @classmethod
    def query_model_query_records_by_model_id(cls, v_sample_id):
        model = repository.query_model_query_records_by_model_id(v_sample_id)
        if model is not None:
            return json.loads(json.dumps(marshal(model, ModelQueryRecordModel.marshal_fields)))
        return None

    @classmethod
    def query_all(cls):
        model = repository.query_all()
        if model is not None:
            return json.loads(json.dumps(marshal(model, ModelQueryRecordModel.marshal_fields)))
        return None
