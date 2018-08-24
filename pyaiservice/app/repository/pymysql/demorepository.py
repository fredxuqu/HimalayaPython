"""
    create by Fred on 2018/8/22
"""
from flask_sqlalchemy import SQLAlchemy

from app.models.demomodel import DemoModel

__author__ = 'Fred'

db = SQLAlchemy()

class DemoRepository():
    
    def save(self, demomodel):
        
#         model1 = DemoModel(title= 'java', 
#                            author = 'john',
#                            binding = 'b11',
#                            publisher = 'csdn',
#                            price = 12.0,
#                            pages = 340,
#                            pubdate = '2018-09-01',
#                            isbn = 'ISBN0000001',
#                            summary = 'mary@example.com',
#                            image = 'mary@example.com.jpg')
        
        try:
            db.session.add(demomodel)
            # commit
            db.commit()
        except:
            # rollback in case there is any error
            pass
    
    
    @classmethod       
    def queryAll(cls):       
        try:
            pass
#             for model in DemoModel.query.all():
#                 print ('title=%s,isbn=%s' %(model.title, model.isbn))
        except:
            print ("Error: unable to fecth data")
                    
    
    @classmethod       
    def query(cls, v_isbn):
        try:
#             model = DemoModel.query.filter_by(isbn=v_isbn).first()
#             print(model.title)
            pass
        except:
            print ("Error: unable to fecth data")
        
        