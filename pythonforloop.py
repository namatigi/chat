#!/usr/bin/python

for letter in "PYTHON":
    print "Current Letter: ",letter



fruits = ['banana','apple','mango']

for fruit in fruits:
    print "Current fruit:",fruit

print "GOOD BYE"


#iterating by index.

for index in range(len(fruits)):
    print "Current fruit:",fruits[index]

print "GOOD MORNING"


for num in range(10,20):
    for i in range(2,num):
        if num % i ==0:
            j=num/i
            print '%d equals %d * %d' % (num,i,j)
            break
    else:
        print num, 'is a prime number'
