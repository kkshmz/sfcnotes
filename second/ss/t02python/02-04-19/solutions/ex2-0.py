'''
// 1. Populate an array with the numbers 1 through 100
// 2, Shuffle it
// 3, Take the first 8 elements of the resulting array.
'''
from random import shuffle

x = range(0,100)
shuffle(x)
y = x[:8]
list.sort(y)
print y
