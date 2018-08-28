"""
    create by Fred on 2018/8/22
"""
from flask import Flask
from flask.globals import current_app

__author__ = 'Fred'

app = Flask(__name__)

# push app to context
# ctx = app.app_context()
# ctx.push()
# currentApp = current_app
# print (currentApp.config['DEBUG'])


with app.app_context():
    currentApp = current_app
    print (current_app.config['DEBUG'])
    
    
class MyResource():
    def __enter__(self):
        print('Connection to resource')
        return self
    
    def __exit__(self, exc_type, exc_value, tb):
        if tb:
            print('process exception')
        else:
            print('process no exception')
        print('Close resource connection')
        return False
      
    def query(self):  
        print('query data')
      
try:  
    with MyResource() as resource:
        1/0
        resource.query()
except Exception as ex:
    print('exception caught! ')
    pass
            
