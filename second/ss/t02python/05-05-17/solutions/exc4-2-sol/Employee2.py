#!/usr/bin/env python

#Example of a simple class

class Employee:
   'Common base class for all employees'
   empCount = 0 #example of class variable
   
   empSalList={}

   def __init__(self, name, salary):
      self.name = name 
      self.salary = salary
      Employee.empCount += 1
      
      self.empSalList[name]=salary
   
   def displayCount(self):
     print "Total Employee %d" % Employee.empCount

   def displayEmployee(self):
      print "Name : ", self.name,  ", Salary: ", self.salary
  
  
   def setname(self,name):
      self.name=name

   def getname(self):
      return self.name

   def setsalary(self,salary):
      self.salary=salary

   def getsalary(self):
      return self.salary

   
   @staticmethod
   def displayCountess():
      return Employee.empCount
   
