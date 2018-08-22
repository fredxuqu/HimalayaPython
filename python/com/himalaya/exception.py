#!/usr/bin/python3

class MyError(Exception):
    def __init__(self, value):
        self.value = value
    def __str__(self):
        return repr(self.value)

while True:
    try:
        x = int(input("Please enter a number: "))
        print (x)
        break
    except ValueError:
        print("Oops!  That was no valid number.  Try again")

# try:
#     raise NameError('HiThere')
# except NameError:
#     print('An exception flew by!')
#     raise
       
try:
    raise MyError('HiThere')
except MyError:
    print('An exception flew by!')
    raise