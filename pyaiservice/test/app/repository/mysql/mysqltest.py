"""
    create by Fred on 2018/8/22
"""
from flask_restful import marshal, fields
import json
import unittest
from test.app.repository.mysql.usertest import User
from test.app.repository.mysql import usertest 

__author__ = 'Fred'


class TestCase(unittest.TestCase):


    def setUp(self):
        unittest.TestCase.setUp(self)


    def tearDown(self):
        unittest.TestCase.tearDown(self)


    def testCreateAll(self):
        usertest.db.create_all()
        admin = User(username='admin', email='admin@example.com')
        usertest.db.session.add(admin)
        usertest.db.session.commit()


    def testSave(self):
        wendy = User(username='wendy', email='wendy@example.com')
        usertest.db.session.add(wendy)
        usertest.db.session.commit()
    
    
    def testQueryById(self):
        user = User.query.filter_by(username='wendy').first()
        print (json.loads(json.dumps(marshal(user, User.marshal_fields))))
    
    
    def testDelete(self):
        user = User.query.filter_by(username='wendy').first()
        print (json.loads(json.dumps(marshal(user, User.marshal_fields))))
        usertest.db.session.delete(user)
        usertest.db.session.commit()
    
    
    def testUpdate(self):
        user = User.query.filter_by(username='wendy').first()
        print (json.loads(json.dumps(marshal(user, User.marshal_fields))))
        user.email='wendynew@example.com'
        usertest.db.session.commit()
    
    
    def testQueryAll(self):
        list = User.query.all()
        print (list.__len__)
        result = []
        for d in list:
            result.append(json.loads(json.dumps(marshal(d, User.marshal_fields))))
            usertest.db.session.delete(d)
        print (result) 
        usertest.db.session.commit()       
    
                 
if __name__ == '__main__':
    unittest.main()
    
    