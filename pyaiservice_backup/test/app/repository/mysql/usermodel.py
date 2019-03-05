from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy import Column, Integer, String
from flask_restful import fields

app = Flask(__name__)

app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql+pymysql://test:Admin#1010@localhost:3306/solr'

db = SQLAlchemy(app)


class User(db.Model):

    v_db = db
    
    __tablename__ = 'TB_USER'
    
    id = Column(Integer, primary_key=True)
    user_name = Column(String(20), unique=True, nullable=False)
    role_id = Column(Integer, nullable=False)
    status = Column(String(1), unique=True, nullable=False)

    marshal_fields = {}
    marshal_fields['id'] = fields.Integer(attribute='id')
    marshal_fields['user_name'] = fields.String(attribute='user_name')
    marshal_fields['role_id'] = fields.String(attribute='role_id')
    marshal_fields['status'] = fields.String(attribute='status')

    def __repr__(self):
        return '<ID%r User %r RoleID %r Status %r>' % (self.id, self.user_name, self.role_id, self.status)
