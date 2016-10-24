#!/usr/bin/env python
#Example on using a class (calling its method, initialising())

class Employee:
   'Common base class for all employees'
   empCount = 0

   def __init__(self, name, salary):
      self.name = name
      self.salary = salary
      Employee.empCount += 1
   
   def displayCount(self):
     print "Total Employee %d" % Employee.empCount

   def displayEmployee(self):
      print "Name : ", self.name,  ", Salary: ", self.salary
      
"This would create first object of Employee class"
emp1 = Employee("Zara", 2000)
"This would create second object of Employee class"
emp2 = Employee("Manni", 5000)

emp1.displayEmployee()
emp2.displayEmployee()
print "Total Employee %d" % Employee.empCount

emp1.age = 78  # Add an 'age' attribute.

print emp1.name
print emp1.age
print emp1.salary

del emp1.age #delete it

#another 
print getattr(emp1, 'age') 
print getattr(emp1,'name')

#modified from source:http://www.tutorialspoint.com/python/python_classes_objects.htm