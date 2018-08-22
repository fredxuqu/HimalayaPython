#!/usr/bin/python3

filepath='python.txt'

with open(filepath) as file_object:
    contents = file_object.read()
print (contents)

# w : override write
# a : append

with open(filepath,'w') as file_object:
    file_object.write("I love programming \r")

print ('\r')

file = open(filepath)
for line in file:
    print (line.strip())
file.close()

print ('\r')

# read file to a collection, each line is a element
with open(filepath) as file_object:
    lines = file_object.readlines()
print(lines)

