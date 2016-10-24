#!/usr/bin/env python

#Example om inheritance, the class "Child" refer to "Parent" hence inherited its data and methods

#This is the way if Parent is in a separate file
#import Parent

class Parent:        # define parent class
   parentAttr = 100
   def __init__(self):
      print "Calling parent constructor"

   def parentMethod(self):
      print 'Calling parent method'

   def setAttr(self, attr):
      Parent.parentAttr = attr

   def getAttr(self):
      print "Parent attribute :", Parent.parentAttr



class Child(Parent): # define child class

#This is the way if Parent is in a separate file
#class Child(Parent.Parent): # define child class
   def __init__(self):
      print "Calling child constructor"

   def childMethod(self):
      print 'Calling child method'

c = Child()          # instance of child
c.childMethod()      # child calls its method
c.parentMethod()     # calls parent's method
c.setAttr(200)       # again call parent's method
c.getAttr()          # again call parent's method


#source: http://www.tutorialspoint.com/python/python_classes_objects.htm
