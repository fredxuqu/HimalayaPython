#!/usr/bin/python3

import os
print (os.getcwd())
os.chdir('d:/workspaces')
print (os.getcwd())
os.system('mkdir test')
print (os.getcwd())
os.removedirs('d:/workspaces/test')