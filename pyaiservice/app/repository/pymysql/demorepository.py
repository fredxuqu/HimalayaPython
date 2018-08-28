"""
    create by Fred on 2018/8/22
"""
from app.models.demomodel import DemoModel

__author__ = 'Fred'


class DemoRepository():
    
    @classmethod
    def save(self, demomodel):               
        try:
            demomodel.save()
        except AttributeError as ex:
            # rollback in case there is any error
            print ("Error: unable to save data")
            print (ex)
        
        
    @classmethod
    def queryAll(cls):       
        try:
            return DemoModel.query.all()
        except:
            print ("Error: unable to fecth data from database")
        return None
        
        
    @classmethod
    def queryByUserName(cls, v_username):
        try:
            return DemoModel.query.filter_by(username = v_username).first()
        except:
            print ("Error: unable to fecth data from database")
        return None
    
    