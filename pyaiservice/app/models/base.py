"""
    create by Fred on 2018/8/22
"""

from datetime import datetime
from contextlib import contextmanager
from sqlalchemy import Column, Integer, SmallInteger
from flask import current_app
from flask_sqlalchemy import SQLAlchemy as _SQLAlchemy, BaseQuery


__author__ = 'Fred'

__all__ = ['db', 'Base']


class SQLAlchemy(_SQLAlchemy):
    @contextmanager
    def auto_commit(self, throw=True):
        try:
            yield
            self.session.commit()
        except Exception as e:
            self.session.rollback()
            current_app.logger.exception('%r' % e)
            if throw:
                raise e


# class Query(BaseQuery):
#     def filter_by(self, **kwargs):
#         if 'status' not in kwargs.keys():
#             kwargs['status'] = 1
#         return super(Query, self).filter_by(**kwargs)


db = SQLAlchemy(query_class=BaseQuery)


class Base(db.Model):
    __abstract__ = True
    version = Column('version', Integer)
    create_time = Column('create_time', Integer)
    modify_time = Column('modify_time', Integer)
    user = Column('user', Integer)
    status = Column(SmallInteger, default=1)


    def __init__(self):
        self.create_time = int(datetime.now().timestamp())
        self.modify_time = int(datetime.now().timestamp())
        self.version = 0
        self.status = 0
        self.user = 'Admin'
        

    @property
    def create_datetime(self):
        if self.create_time:
            return datetime.fromtimestamp(self.create_time)
        else:
            return None


    def delete(self):
        self.status = 0


    def set_attrs(self, attrs):
        for key, value in attrs.items():
            if hasattr(self, key) and key != 'id':
                setattr(self, key, value)

