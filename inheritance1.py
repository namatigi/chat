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


dev1 = Developer('Leonard','Mangu',100000,'C++')

dev2 = Developer('Ombeni','Aidani',200000,'PHP')
#
# print(help(Developer))

# print(dev1.pay)
# dev1.apply_raise()
# print(dev1.pay)
# print(dev1.email)
# print(dev2.email)

# print(dev1.prog_lang)
# print(dev2.prog_lang)

mgr1 = Manager('Leonard','Smith',900000,[dev1])


#
# print mgr1.email
#
# mgr1.add_emp(dev2)
# print mgr1.print_emps()

# mgr1.remove_emp(dev1)
# print mgr1.print_emps()



print(issubclass(Manager,Employee))

print(isinstance(mgr1,Developer))
