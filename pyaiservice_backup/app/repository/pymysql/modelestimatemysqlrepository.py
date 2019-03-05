"""
    create by Fred on 2018/8/22
"""
from app.models.modelqueryrecordmodel import ModelQueryRecordModel
from app.models.statstrategyqueryrecordmodel import StatStrategyRecordModel
from app.models.samplerecordmodel import SampleRecordModel

__author__ = 'Fred'


class ModelEstimateMysqlRepository:

    @classmethod
    def query_all_sample(cls):
        try:
            v_query = ModelQueryRecordModel.query
            v_query.filter_by(sample_id=10)
            v_query.paginate(1, 10)
            return v_query.all()
        except Exception as ex:
            print("Error: " + ex)
        return None

    @classmethod
    def query_sample_model_records_paginate(cls, v_sample_id, v_model_id, page_size, current_page, is_sort_asc):
        try:
            # join tables and build a query object
            query = ModelQueryRecordModel.global_db.session\
                    .query(ModelQueryRecordModel.batno, ModelQueryRecordModel.score, SampleRecordModel.result)\
                    .filter(ModelQueryRecordModel.batno == SampleRecordModel.batno) \
                    .filter(SampleRecordModel.sample_id == v_sample_id) \
                    .filter(ModelQueryRecordModel.model_id == v_model_id)

            # sorting
            if is_sort_asc is not None and is_sort_asc is True:
                query = query.order_by(ModelQueryRecordModel.score.asc())
            else:
                query = query.order_by(ModelQueryRecordModel.score.desc())

            # paginate
            query = query.limit(page_size).offset((int(current_page) - 1) * page_size)

            return query.all()
        except Exception as ex:
            print("Error: " + ex)
        return None

    @classmethod
    def query_sample_model_strategy_records_paginate(
                    cls, v_sample_id, v_model_id, v_strategy_id, page_size, current_page, is_sort_asc):
        try:
            # join tables and build a query object
            query = StatStrategyRecordModel.global_db.session \
                .query(StatStrategyRecordModel.batno, StatStrategyRecordModel.score, SampleRecordModel.result) \
                .filter(StatStrategyRecordModel.batno == SampleRecordModel.batno)\
                .filter(SampleRecordModel.sample_id == v_sample_id)\
                .filter(StatStrategyRecordModel.model_id == v_model_id)\
                .filter(StatStrategyRecordModel.strategy_id == v_strategy_id)

            # sorting
            if is_sort_asc is not None and is_sort_asc is True:
                query = query.order_by(StatStrategyRecordModel.score.asc())
            else:
                query = query.order_by(StatStrategyRecordModel.score.desc())

            # paginate
            query = query.limit(page_size).offset((int(current_page) - 1) * page_size)

            return query.all()
        except Exception as ex:
            print("Error: " + ex)
        return None

