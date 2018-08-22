#!/usr/bin/python
 
import re
print(re.match('www', 'www.runoob.com').span())
print(re.match('com', 'www.runoob.com'))

line = "Cats are smarter than dogs"
 
matchObj = re.match( r'(.*) are (.*?) .*', line, re.M|re.I)
 
if matchObj:
    print ("matchObj.group() : ", matchObj.group())
    print ("matchObj.group(1) : ", matchObj.group(1))
    print ("matchObj.group(2) : ", matchObj.group(2))
else:
    print ("No match!!")
    
    
####################
##  search        ##
####################
    
print(re.search('www', 'www.runoob.com').span())
print(re.search('com', 'www.runoob.com').span())
 
searchObj = re.search( r'(.*) are (.*?) .*', line, re.M|re.I)
 
if searchObj:
    print ("searchObj.group() : ", searchObj.group())
    print ("searchObj.group(1) : ", searchObj.group(1))
    print ("searchObj.group(2) : ", searchObj.group(2))
else:
    print ("Nothing found!!")
    

####################
##  Replace       ##
####################
phone = "2004-959-559 # this is a phone number"
 
# delete comments
num = re.sub(r'#.*$', "", phone)
print ("Phone number : ", num)
 
# remove non-digital character
num = re.sub(r'\D', "", phone)
print ("Phone number : ", num)
    

# matched number times 2
def double(matched):
    value = int(matched.group('value'))
    return str(value * 2)
 
s = 'A23G4HFD567'
print(re.sub('(?P<value>\d+)', double, s)) 


pattern = re.compile(r'\d+')                        # at least match a digital number
m = pattern.match('one12twothree34four')            # search header, unmatched.
print m

m = pattern.match('one12twothree34four', 2, 10)     # search from 'e', unmatched.
print m

m = pattern.match('one12twothree34four', 3, 10)     # search from '1' matched.
print m                                             # return a match object
print m.group(0)
print m.start(0)
print m.end(0)
print m.span(0)
