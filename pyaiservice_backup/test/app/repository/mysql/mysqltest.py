"""
    create by Fred on 2018/8/22
"""
from flask_restful import marshal, fields
import json
import unittest
from test.app.repository.mysql.rolemodel import Role
from test.app.repository.mysql.usermodel import User

__author__ = 'Fred'


class TestCase(unittest.TestCase):


    def setUp(self):
        unittest.TestCase.setUp(self)


    def tearDown(self):
        unittest.TestCase.tearDown(self)

    def testQueryAllRole(self):
        list = Role.query.all()
        print(list.__len__)
        result = []
        for d in list:
            result.append(json.loads(json.dumps(marshal(d, Role.marshal_fields))))
            print(result)

    def testQueryAllUser(self):
        list = User.query.all()
        print(list.__len__)
        print(list)
        result = []
        for d in list:
            result.append(json.loads(json.dumps(marshal(d, Role.marshal_fields))))
            print(d)

    def testQueryAllUserByName(self):
        user = User.query.filter_by(user_name='Fred').all()
        print(user)

    def testQueryAllUserByPaging(self):
        user = User.query.all()
        print(user)
        # page size from 1
        page_size = 3
        current_page = 2
        query = User.query.filter_by(status='A')
        query = query.limit(page_size).offset((int(current_page) - 1) * page_size)
        user = query.all()
        print(user)

    def testQueryAllUserAndRole(self):
        query = User.query.join(Role, User.role_id == Role.id)
        query = query.filter_by(status='A')
        list = query.all()
        print(list)

    def testQueryAllUserBySession(self):
        query = User.v_db.session.query(Role)
        list = query.order_by(Role.id, True).all()
        print(list)

    def testJoinUserAndRole(self):
        page_size = 2
        current_page = 1
        all_records = []
        flag = True
        while flag:
            query = User.v_db.session.query(User.id, User.user_name, Role.role_name).filter(User.role_id == Role.id)
            query = query.order_by(User.id).limit(page_size).offset((int(current_page) - 1) * page_size)
            list = query.all()
            if list is not None and len(list) > 0:
                for item in list:
                    v_1 = item[0]
                    v_2 = item[1]
                    v_3 = item[2]
                    all_records.append(item)
                print(list)
            if list is None or len(list) == 0:
                flag = False
            current_page = current_page + 1
        print(all_records)
        print("Query End")

"""
    def testCreateAll(self):
        rolemodel.db.create_all()
        admin = User(username='admin', email='admin@example.com')
        rolemodel.db.session.add(admin)
        rolemodel.db.session.commit()
        
        
    def testSave(self):
        wendy = User(username='wendy', email='wendy@example.com')
        rolemodel.db.session.add(wendy)
        rolemodel.db.session.commit()
    
    
    def testQueryById(self):
        user = User.query.filter_by(username='wendy').first()
        print (json.loads(json.dumps(marshal(user, User.marshal_fields))))
    
    
    def testDelete(self):
        user = User.query.filter_by(username='wendy').first()
        print (json.loads(json.dumps(marshal(user, User.marshal_fields))))
        rolemodel.db.session.delete(user)
        rolemodel.db.session.commit()
    
    
    def testUpdate(self):
        user = User.query.filter_by(username='wendy').first()
        print (json.loads(json.dumps(marshal(user, User.marshal_fields))))
        user.email='wendynew@example.com'
        rolemodel.db.session.commit()
    
    
    def testQueryAll(self):
        list = User.query.all()
        print (list.__len__)
        result = []
        for d in list:
            result.append(json.loads(json.dumps(marshal(d, User.marshal_fields))))
            rolemodel.db.session.delete(d)
        print (result) 
        rolemodel.db.session.commit()
"""
                 
if __name__ == '__main__':
    unittest.main()
    
    