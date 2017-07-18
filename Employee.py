class Employee:
    'Common base class for all employee'

    empCount = 0

    def __init__(self,name,salary):
        self.name = name
        self.salary = salary
        Employee.empCount +=1

    def displayCount(self):
        print "Total Employee %d" %Employee.empCount


    def displayEmployee(self):
        print "Name: ",self.name, ", Salary: ",self.salary


"This would create first object of Employee class"
emp1 = Employee('Leonard',1000000);

"This would create second object of Employee class"
emp2 = Employee("Mangu",2000000);

emp1.displayEmployee()

emp2.displayEmployee()

emp2.displayCount()

emp1.age = 100

print getattr(emp1,'age')

if(hasattr(emp1,'age')):
    print "This has employee age attribute"

print "Employee.__doc__: ",Employee.__doc__
print "Employee.__name__: ",Employee.__name__
print "Employee.__module__: ",Employee.__module__
print "Employee.__bases__: ",Employee.__bases__
print "Employee.__dict__: ",Employee.__dict__
