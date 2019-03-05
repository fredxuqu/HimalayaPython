"""
    create by Fred on 2018/8/22
"""
from flask_pymongo import PyMongo

__author__ = 'Fred'

mongodb = PyMongo()


class BaseMongoRepository:

    @classmethod
    def insert(self, jsonstr):               
        try:
            mongodb.db.ivwoe.insert({"name":"save client"})
        except AttributeError as ex:
            # rollback in case there is any error
            print ("Error: unable to save data")
            print (ex)
        
        
    @classmethod
    def queryAll(cls):       
        try:
            return mongodb.db.ivwoe.find()
        except:
            print ("Error: unable to fecth data from database")
        return None
