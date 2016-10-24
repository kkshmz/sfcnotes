#!/usr/bin/env python

#Example of a simple class

class Employee:
   'Common base class for all employees'
   empCount = 0 #example of class variable

   def __init__(self, name, salary):
      self.name = name 
      self.salary = salary
      Employee.empCount += 1
   
   def displayCount(self):
     print "Total Employee %d" % Employee.empCount

   def displayEmployee(self):
      print "Name : ", self.name,  ", Salary: ", self.salary
  

emp1=Employee("Ucu",90)
emp2=Employee("Husni",80)
emp3=Employee("Murai",200)

emp1.displayEmployee()
emp2.displayEmployee()
emp3.displayEmployee()

emp1.displayCount()