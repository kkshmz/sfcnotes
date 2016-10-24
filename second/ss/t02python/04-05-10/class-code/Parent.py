#!/usr/bin/env python

#Example of inheritance. This is the class than can be used by other class as "parent" (class name can be anything, "Parent" is just an example)
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
      
#source: http://www.tutorialspoint.com/python/python_classes_objects.htm
      


