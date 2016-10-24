#!/usr/bin/env python
from scipy import misc
import numpy as np

#read image file and covert it into "lena" which is a NumPy Array format
lena = misc.imread('lena.png')

#print infos/properties of lena
print type(lena)
print lena.dtype

print lena.shape
#you can get lena's size into variables
lx, ly = lena.shape

#SOME BASIC MANIPULATION(try it yourself!)
#Cropping
#crop_lena = lena[lx / 4: - lx / 4, ly / 4: - ly / 4]
# up <-> down flip
#flip_ud_lena = np.flipud(lena)
# rotation
#rotate_lena = ndimage.rotate(lena, 45)
#rotate_lena_noreshape = ndimage.rotate(lena, 45, reshape=False)
#EYE matrix
#d=np.eye(480)
#leni=np.dot(lena,d)


#MORE ADVANCED MANIPULATION (try it yourself!)
#blurred_lena = ndimage.gaussian_filter(lena, sigma=3)
#very_blurred = ndimage.gaussian_filter(lena, sigma=5)
#increase the weight of edges by adding an approximation of the Laplacian:
#filter_blurred_l = ndimage.gaussian_filter(blurred_l, 1)
#alpha = 30
#sharpened = blurred_l + alpha * (blurred_l - filter_blurred_l)
#l = misc.lena()
#l = l[230:310, 210:350]
#noisy = l + 0.4 * l.std() * np.random.random(l.shape)
#gauss_denoised = ndimage.gaussian_filter(noisy, 2)
#med_denoised = ndimage.median_filter(noisy, 3)






#SAVE IT TO OUTPUT 
#"leni.png" is the manipulated image
misc.imsave('leni.png',lena)
