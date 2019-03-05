#!/usr/bin/python3
import sys,os
# import pandas as pd

workdir_path="C:/Users/xuqu/git/HimalayaPython/"

# pd.read_csv()

def cur_file_path():
    path = sys.path[0]
    if os.path.isdir(path):
        return path
    if os.path.isfile(path):
        return os.path.dirname(path)

def hello():
    print ('Hello world!')
    
def sum(a, b):
    return a + b

hello()

sum = sum(10, 101)
print (sum)
print (cur_file_path())
print (workdir_path)