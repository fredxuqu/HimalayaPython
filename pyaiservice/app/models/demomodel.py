"""
    create by Fred on 2018/8/22
"""
from sqlalchemy import Column, Integer, String
from flask_sqlalchemy import SQLAlchemy

__author__ = 'Fred'

db = SQLAlchemy()

class DemoModel(db.Model):
    
    id = Column(Integer, primary_key=True, autoincrement=True)
    title = Column(String(50), nullable=False)
    author = Column(String(30), default='--')
    binding = Column(String(20))
    publisher = Column(String(50))
    price = Column(String(20))
    pages = Column(Integer)
    pubdate = Column(String(20))
    isbn = Column(String(15), nullable=False, unique=True)
    summary = Column(String(1000))
    image = Column(String(50))
    
    
    def __init__(self, title, author, binding, publisher,price,pages,pubdate,isbn,summary,image):
        self.title = title
        self.author = author
        self.binding = binding
        self.publisher = publisher
        self.price = price
        self.pages = pages
        self.pubdate = pubdate
        self.isbn = isbn
        self.summary = summary
        self.image = image    
    
    
    def save(self):
        cursor = db.cursor()
        sql = """INSERT INTO demo_model(title, author, binding, publisher,price,pages,pubdate,isbn,summary,image)
         VALUES ('Mac', 'Mohan', 20, 'M', 2000)"""
        
        try:
            cursor.execute(sql)
            # commit
            db.commit()
        except:
            # rollback in case there is any error
            db.rollback()
            # close connection
            db.close()
            
            