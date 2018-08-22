#!/usr/bin/python3

class MyClass:
    """A very simple instance"""
    i = 12345
    def f(self):
        return 'hello world'
       
    def __init__(self, v_i):
        self.i = v_i
    
class Complex:
    def __init__(self, realpart, imagpart):
        self.r = realpart
        self.i = imagpart
        
class People:
    name = ''
    age = 0
    def __init__(self, name, age):
        self.name = name
        self.age = age    
    def speak(self):
        print ("My name is %s, I am %d" %(self.name, self.age))
    def call(self):
        print ("People Call %s" %(self.name))
        
class Student(People):
    grade = ''
    def __init__(self, name, age, grade):
        People.__init__(self, name, age)
        self.grade = grade
    def speak(self):
        People.speak(self) 
        print ("I am in grade %s"%(self.grade))
    def call(self):
        print ("Student Call %s" %(self.name))  
        
class Parent:
    def myMethod(self):
        print ('Parent method')
 
class Child(Parent):
    def myMethod(self):
        print ('Child method')
        
class JustCounter:
    __secretCount = 0  # private attributed
    publicCount = 0 # public attributed

    def count(self):
        self.__secretCount += 1
        self.publicCount += 1
        print (self.__secretCount)
    
    def getSecretCount(self):
        return self.__secretCount
    
    def __privateMethod(self):
        print ("This is private method");
    
    def publicMethod(self):
        self.__privateMethod()
        
        
        
    