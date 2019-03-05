"""
    create by Fred on 2018/8/22
"""
from app.models.statstrategyqueryrecordmodel import StatStrategyRecordModel

__author__ = 'Fred'


class StatStrategyRecordMysqlRepository:
    
    @classmethod
    def save(cls, sample_model):
        try:
            sample_model.save()
        except AttributeError as ex:
            # rollback in case there is any error
            print("Error: unable to save data")
            print(ex)

    @classmethod
    def query_all(cls):
        try:
            return StatStrategyRecordModel.query.all()
        except Exception as ex:
            print("Error: " + ex)
        return None

    @classmethod
    def query_strategy_query_records_by_strategy_id(cls, v_strategy_id):
        try:
            return StatStrategyRecordModel.query.filter_by(strategy_id=v_strategy_id).first();
        except Exception as ex:
            print("Error: " + ex)
        return None
