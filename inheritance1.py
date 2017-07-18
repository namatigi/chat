#!/usr/bin/python

class Employee:


    raise_amt = 1.04

    def __init__(self,first,last,pay):
        self.first = first
        self.last = last
        self.pay = pay
        self.email = first + '.'+ last +"@phronetec.com"


    def fullname(self):
        return '{} {}'.format(self.first,self.last)


    def apply_raise(self):
        self.pay = int(self.pay * self.raise_amt)


    def __repr__(self):
        return "Employee('{}','{}','{}')".format(self.first,self.last,self.pay)

    def __str__(self):
        #  pass
        return '{} - {}'.format(self.fullname(),self.email)


    def __add__(self,other):
        return self.pay + other.pay


    def __len__(self):
        return len(self.fullname())



class Developer(Employee):
    raise_amt = 1.10

    def __init__(self,first,last,pay,prog_lang):
        # super().__init__(first,last,pay)
        Employee.__init__(self,first,last,pay)
        self.prog_lang = prog_lang



class Manager(Employee):

    def __init__(self,first,last,pay,employees= None):
        Employee.__init__(self,first,last,pay)
        if employees is None:
            self.employees = []
        else:
            self.employees = employees


    def add_emp(self,emp):
        if emp not in self.employees:
            self.employees.append(emp)


    def remove_emp(self,emp):
        if emp in self.employees:
            self.employees.remove(emp)


    def print_emps(self):
        for emp in self.employees:
            print('--->',emp.fullname())


dev1 = Employee('Leonard','Mangu',100000)

dev2 = Employee('Ombeni','Aidani',200000)


# print(1+2)
#
# print(int.__add__(1,2))

# print(dev1 + dev2)

print(len('LEONARD'))

print('TEST'.__len__())

print(len(dev1))

# print(str.__add__('a','b'))
# print(dev1)

# print(repr(dev1))
# print(str(dev1))
#
# print(dev1.__str__())
# print(dev1.__repr__())
# #
# print(help(Developer))

# print(dev1.pay)
# dev1.apply_raise()
# print(dev1.pay)
# print(dev1.email)
# print(dev2.email)

# print(dev1.prog_lang)
# print(dev2.prog_lang)

# mgr1 = Manager('Leonard','Smith',900000,[dev1])


#
# print mgr1.email
#
# mgr1.add_emp(dev2)
# print mgr1.print_emps()

# mgr1.remove_emp(dev1)
# print mgr1.print_emps()



# print(issubclass(Manager,Employee))
#
# print(isinstance(mgr1,Developer))
