"""
    create by Fred on 2018/8/22
"""
from app.entity.sampleentity import SampleEntity

__author__ = 'Fred'


class SampleRepository:
    
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
            return SampleEntity.query.all()
        except Exception as e:
            print("Error: unable to fetch data from database, " + e)
        return None

    @classmethod
    def query_sample_by_id(cls, v_sample_id):
        try:
            query = SampleEntity.query.filter_by(id=v_sample_id)
            sample = query.first()
            return sample
        except Exception as e:
            print("Error: unable to fetch sample data from database, " + e)
        return None

