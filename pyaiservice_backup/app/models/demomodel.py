"""
    create by Fred on 2018/8/22
"""
from flask_restful import fields
from sqlalchemy import Column, Integer, String
from app.models.base import db, Base

__author__ = 'Fred'


class UserModel(Base):

    __tablename__ = 'TB_USER'

    id = Column(Integer, primary_key=True)
    user_name = Column(String(20), unique=True, nullable=False)
    email = Column(String(50), unique=True, nullable=False)
    role_id = Column(Integer, nullable=False)
    status = Column(String(1), unique=True, nullable=False)

    marshal_fields = {}
    marshal_fields['id'] = fields.Integer(attribute='id')
    marshal_fields['user_name'] = fields.String(attribute='user_name')
    marshal_fields['email'] = fields.String(attribute='email')
    marshal_fields['role_id'] = fields.String(attribute='role_id')
    marshal_fields['status'] = fields.String(attribute='status')

    def __init__(self, v_user_name, v_email, v_role_id, v_status):
        Base.__init__(self)
        self.user_name = v_user_name
        self.email = v_email
        self.role_id = v_role_id
        self.status = v_status

    def __repr__(self):
        return '{"id":%r,"user_name":%r, "email": %r, "role_id": %r, "status": %r}' \
               % (self.id, self.user_name, self.email, self.role_id, self.status)

    def save(self):
        try:
            db.session.add(self)
            db.session.commit()
        except Exception as e:
            print("Error: " + e)
            db.session.rollback()
            return False
        return True

    def delete(self):
        try:
            db.session.delete(self)
            db.session.commit()
        except Exception as e:
            print("Error: " + e)
            db.session.rollback()
            return False
        return True

    def get(self):
        try:
            return db.session.get(self.id)
        except Exception as e:
            print("Error: " + e)
        return None
