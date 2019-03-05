"""
    create by Fred on 2018/8/22
"""
from flask_restful import marshal
from app.entity.sampleentity import SampleEntity
from app.repository.pymysql.samplerepository import SampleRepository
import json

__author__ = 'Fred'


repository = SampleRepository()


class SampleService:

    @classmethod
    def query_all(cls):
        v_list = SampleRepository.query_all()
        if v_list is not None:
            return json.loads(json.dumps(marshal(v_list, SampleEntity.marshal_fields)))
        return None

    @classmethod
    def query_by_sample_id(cls, v_sample_id):
        v_model = SampleRepository.query_sample_by_id(int(v_sample_id))
        if v_model is not None:
            return json.loads(json.dumps(marshal(v_model, SampleEntity.marshal_fields)))
        return None

