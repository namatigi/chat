#!/usr/bin/python

Money = 2000


def addMoney():
    global Money
    Money = Money + 1


print Money
addMoney()
print Money


import math

content = dir(math)

print content
