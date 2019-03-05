"""
    create by Fred on 2018/8/22
"""
from flask_restful import marshal
from app.models.samplemodel import SampleModel
from app.repository.pymysql.samplemysqlrepository import SampleMysqlRepository
import json

__author__ = 'Fred'


repository = SampleMysqlRepository()


class SampleMySQLService:

    @classmethod
    def query_all(cls):
        v_list = SampleMysqlRepository.query_all()
        if v_list is not None:
            return json.loads(json.dumps(marshal(v_list, SampleModel.marshal_fields)))
        return None

    @classmethod
    def query_by_sample_id(cls, v_sample_id):
        v_model = SampleMysqlRepository.query_sample_by_id(int(v_sample_id))
        if v_model is not None:
            return json.loads(json.dumps(marshal(v_model, SampleModel.marshal_fields)))
        return None

