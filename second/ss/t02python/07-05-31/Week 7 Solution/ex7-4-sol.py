#!/usr/bin/env python
from scipy import misc
import numpy as np
from scipy import ndimage

lena = misc.imread('lena.png')

#use numpy method of "flipud" and "rotate" to manipulate lena.png
# up <-> down flip
flip_ud_lena = np.flipud(lena)
rotate_lena = ndimage.rotate(lena, 45)
lx, ly = lena.shape
#use this equation to crop lena:
crop_lena = lena[lx / 4: - lx / 4, ly / 4: - ly / 4]

#save the outputs to "lena_flip.png", "lena_rotate.png", "lena_crop.png"
misc.imsave('lena_flip.png',flip_ud_lena)
misc.imsave('lena_rotate.png',rotate_lena)
misc.imsave('lena_crop.png',crop_lena)
