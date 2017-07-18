#!/usr/bin/python

class Employee:


    raise_amt = 1.04

    def __init__(self,first,last):
        self.first = first
        self.last = last
        # self.pay = pay
        # self.email = first + '.'+ last +"@phronetec.com"

    @property
    def email(self):
        return '{}.{}@phroneetec.com'.format(self.first,self.last)

    @property
    def fullname(self):
        return '{} {}'.format(self.first,self.last)

    @fullname.setter
    def fullname(self,name):
        first,last = name.split('-')
        self.first= first
        self.last = last

emp1 = Employee('John','Mangu')

emp1.fullname = 'James-Mangu'

print(emp1.first)
print(emp1.email)
print(emp1.fullname)
