"""
    create by Fred on 2018/8/22
"""
from flask_restful import marshal
from app.entity.statstrategyqueryrecordentity import StatStrategyRecordEntity
from app.repository.pymysql.statstrategyqueryrecordrepository import StatStrategyRecordRepository
import json

__author__ = 'Fred'


repository = StatStrategyRecordRepository()


class StrategyQueryRecordService:

    @classmethod
    def query_strategy_query_records_by_strategy_id(cls, v_strategy_id):
        v_model = repository.query_strategy_query_records_by_strategy_id(v_strategy_id)
        if v_model is not None:
            return json.loads(json.dumps(marshal(v_model, StatStrategyRecordEntity.marshal_fields)))
        return None

    @classmethod
    def query_all(cls):
        v_model = repository.query_all()
        if v_model is not None:
            return json.loads(json.dumps(marshal(v_model, StatStrategyRecordEntity.marshal_fields)))
        return None
