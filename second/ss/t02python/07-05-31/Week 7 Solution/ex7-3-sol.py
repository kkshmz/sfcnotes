#!/usr/bin/env python
import scipy
from scipy import misc
import numpy as np

#read image file and covert it into "lena" which is a NumPy Array format
lena = misc.imread('lena.png')

#find out the size of lena.png using .shape method 
lx, ly = lena.shape

#generate identity matrix of the same size.
#
d=np.eye(lx,ly)

#perform dot(multiply operation)
leni=np.dot(lena,d)

#perform dot(multiply operation), save the output to leni.png
misc.imsave('leni.png',leni)
