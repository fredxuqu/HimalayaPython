from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy import Column, Integer, String
from flask_restful import fields

app = Flask(__name__)

app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql+pymysql://test:Admin#1010@localhost:3306/solr'

db = SQLAlchemy(app)


class Role(db.Model):
    
    __tablename__ = 'TB_ROLE'
    
    id = Column(Integer, primary_key=True)
    role_name = Column(String(20), unique=True, nullable=False)
    status = Column(String(1), unique=True, nullable=False)

    marshal_fields = {}
    marshal_fields['id'] = fields.Integer(attribute='id')
    marshal_fields['role_name'] = fields.String(attribute='role_name')
    marshal_fields['status'] = fields.String(attribute='status')

    def __repr__(self):
        return '<Role %r>' % self.role_name
