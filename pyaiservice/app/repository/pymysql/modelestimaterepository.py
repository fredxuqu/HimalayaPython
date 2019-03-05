"""
    create by Fred on 2018/8/22
"""
from app.entity.modelqueryrecordentity import ModelQueryRecordEntity
from app.entity.statstrategyqueryrecordentity import StatStrategyRecordEntity
from app.entity.samplerecordentity import SampleRecordEntity

__author__ = 'Fred'


class ModelEstimateRepository:

    @classmethod
    def query_all_sample(cls):
        try:
            v_query = ModelQueryRecordEntity.query
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
            query = ModelQueryRecordEntity.global_db.session\
                    .query(ModelQueryRecordEntity.batno, ModelQueryRecordEntity.score, SampleRecordEntity.result)\
                    .filter(ModelQueryRecordEntity.batno == SampleRecordEntity.batno) \
                    .filter(SampleRecordEntity.sample_id == v_sample_id) \
                    .filter(ModelQueryRecordEntity.model_id == v_model_id)

            # sorting
            if is_sort_asc is not None and is_sort_asc is True:
                query = query.order_by(ModelQueryRecordEntity.score.asc())
            else:
                query = query.order_by(ModelQueryRecordEntity.score.desc())

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
            query = StatStrategyRecordEntity.global_db.session \
                .query(StatStrategyRecordEntity.batno, StatStrategyRecordEntity.score, SampleRecordEntity.result) \
                .filter(StatStrategyRecordEntity.batno == SampleRecordEntity.batno)\
                .filter(SampleRecordEntity.sample_id == v_sample_id)\
                .filter(StatStrategyRecordEntity.model_id == v_model_id)\
                .filter(StatStrategyRecordEntity.strategy_id == v_strategy_id)

            # sorting
            if is_sort_asc is not None and is_sort_asc is True:
                query = query.order_by(StatStrategyRecordEntity.score.asc())
            else:
                query = query.order_by(StatStrategyRecordEntity.score.desc())

            # paginate
            query = query.limit(page_size).offset((int(current_page) - 1) * page_size)

            return query.all()
        except Exception as ex:
            print("Error: " + ex)
        return None

