#!/usr/bin/python3

var1 = 101
if var1 > 100:
    print ("var1 more than 100")
elif var1 < 100:
    print ("var1 less than 100")
else:
    print ("var1 equals 100")

n = 100
sum = 0
i = 0
while i <= n:
    sum += i
    i += 1

print ("sum is " , sum)

for j in range(10):
    print (j)

companies = ["baidu","google","Alibaba","Pycredit"]
for company in companies:
    print (company)

num = int(input('please input a number:'))
print ('input is ' , num)

