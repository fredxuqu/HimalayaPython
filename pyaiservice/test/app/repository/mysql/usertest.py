from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy import Column, Integer, String
from flask_restful import fields

app = Flask(__name__)

app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql+pymysql://test:Admin#1010@localhost:3306/solr'

db = SQLAlchemy(app)


class User(db.Model):
    
    __tablename__ = 'tb_user'
    
    id = Column(Integer, primary_key=True)
    username = Column(String(80), unique=True, nullable=False)
    email = Column(String(120), unique=True, nullable=False)

    marshal_fields = {}
    marshal_fields['id'] = fields.Integer(attribute='id')
    marshal_fields['username'] = fields.String(attribute='username')
    marshal_fields['email'] = fields.String(attribute='email')

    def __repr__(self):
        return '<User %r>' % self.username
    