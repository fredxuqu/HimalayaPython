"""
    create by Fred on 2018/8/22
"""
import unittest
from app.exception.MyException import MyException
from app.exception.MyException import testRaise
from app.exception.MyException import PreconditionsException


__author__ = 'Fred'
    

class TestCase(unittest.TestCase):

    def setUp(self):
        unittest.TestCase.setUp(self)

    def tearDown(self):
        unittest.TestCase.tearDown(self)

    def testexception(self):
        try:
            raise MyException("DSFASDFASDFASDF")
        except MyException as e:
            print('got it (message: {})'.format(e.message))

    def testexception1(self):
        try:
            testRaise()
        except PreconditionsException as e:
            print(e)


if __name__ == '__main__':
    unittest.main()
