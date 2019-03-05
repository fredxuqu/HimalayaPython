"""
    create by Fred on 2018/8/22
"""
from app.models.demomodel import UserModel

__author__ = 'Fred'


class DemoMysqlRepository:
    
    @classmethod
    def save(cls, demo_model):
        try:
            demo_model.save()
        except AttributeError as ex:
            # rollback in case there is any error
            print("Error: unable to save data")
            print(ex)

    @classmethod
    def query_all(cls):
        try:
            return UserModel.query.all()
        except Exception as ex:
            print("Error: " + ex)
        return None

    @classmethod
    def query_by_username(cls, v_username):
        try:
            return UserModel.query.filter_by(user_name=v_username).first()
        except Exception as ex:
            print("Error: " + ex)
        return None
