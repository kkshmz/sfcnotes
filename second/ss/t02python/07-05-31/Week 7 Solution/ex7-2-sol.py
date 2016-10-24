#!/usr/bin/env python
#-*- coding: utf-8 -*-

import json
import numpy as np

a = open('ex-input-format4.json')
b = open('ex-input-format5.json')

aread =json.loads(a.read())
bread =json.loads(b.read())

#convert the contents into NumPy Array
A=np.array(aread)
B=np.array(bread)

#multiplication(dot) matrix 
C=np.dot(A,B)

#you will have to convert multiplication result (NumPy Array format) into list format before saving into output file using. convert it using
#np.array([[1,2,3],[4,5,6]]).tolist()

CL=np.array(C).tolist()


#save the output to a file “matrixmult.json”
with open('matrixmult.json', 'wb') as wf:
    json.dump(CL, wf)


