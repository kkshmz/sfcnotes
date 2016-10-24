#!/usr/bin/env python

def multiply(x, y):
  '''
  Multiply two numbers
  '''
  return x*y

def intersect(s_a, s_b):
  '''
  This function returns a list of elements
  that are in both s_a and s_b
  '''
  res = []
  for x in s_a:
    if x in s_b:
      res.append(x)
  return res

if __name__ == '__main__':
  print multiply(2,2.5)
  a_list = [1,2,3]
  b_set = {2, 3, 4}
  print intersect(a_list, b_set)


