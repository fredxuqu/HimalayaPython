#!/usr/bin/python3
from com.himalaya.oop import JustCounter
from com.himalaya.oop import MyClass
from com.himalaya.oop import Complex
from com.himalaya.oop import Student
from com.himalaya.oop import Child

# initializing
x = MyClass(100)
 
# operation
print("MyClass property i : ", x.i)
print("MyClass call method f() : ", x.f())

x = Complex(3.0, -4.5)
print(x.r, x.i)

s = Student('fred',22,2)
s.speak()

#super(Student, s).call()

c = Child()
c.myMethod()
# Method in super class can't not be called
#super(Child,c).myMethod() 

counter = JustCounter()
counter.count()
counter.count()
print (counter.publicCount)
# print (counter.__secretCount)
print (counter.getSecretCount())

counter.publicMethod()
# counter.__privateMethod();     # private method can't be called
