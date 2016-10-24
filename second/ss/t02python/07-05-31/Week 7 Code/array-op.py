#!/usr/bin/env python
from numpy import *

a=[[12,3,40],[8,0,100],[99,10,25]]
b=[[11,22,33],[44,55,66],[77,88,99]]

#converting "list" to Numpy Array, represnting 3x3 matrix
A=array(a)
B=array(b)

#or you can delcare an array manually
MyArray=array([12,3,40],[8,0,100],[99,10,25])

#Transpose
AT=A.T

#Slicing
#second row
B1row=B[1,:]
#second column
B1col=B[:,1]
#sliced
Bslice = B[:2, 1:3]

#Indexing
print B[1,2]
B[1,2]=500

#Looping
for row in B:
    print row
    
for element in B.flat:
    print element,

#addition
F=A+B

#multiplication(scalar)
A3=A*3

#multiplication(dot) matrix 
C=dot(A,B)

#generating Eye Matrix 4x4
EyeM=eye(4)

#All one 4x4
OneM=one(4)

#generate using python "range"


print A.shape
print A.dtype
print A.ndim

RangeM=array(range(1,20))



