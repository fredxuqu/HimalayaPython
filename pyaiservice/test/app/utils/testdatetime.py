"""
    create by Fred on 2018/8/22
"""
import unittest
import datetime
import time

__author__ = 'Fred'


class TestCase(unittest.TestCase):

    def setUp(self):
        unittest.TestCase.setUp(self)

    def tearDown(self):
        unittest.TestCase.tearDown(self)

    def test_marshal(self):
        times = "2018-01-03 00:00:00,2018-03-09 00:00:00"
        time_array = times.split(",")
        print(time_array[0])
        print(time_array[1])

    def test_time_time(self):
        print(time.time())
        a = 1000000000.0 * 1000000000000.000000000
        print(time.time())

    def test_time(self):
        # 上月第一天和最后一天
        print(datetime.datetime.now())
        print(datetime.datetime.now() + datetime.timedelta(hours=-1))

    # 本月第一天和最后一天
    def test_get_this_month(self):
        now = datetime.datetime.now()
        this_month_start = datetime.datetime(now.year, now.month, 1)
        this_month_end = datetime.datetime(now.year, now.month + 1, 1) - datetime.timedelta(days=1)
        print(this_month_start)
        print(this_month_end)

if __name__ == '__main__':
    unittest.main()

