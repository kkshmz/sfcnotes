#!/usr/bin/env python

#this line is to be completed(refer to teaching material)

print sys.path
print "\n\n"

if len(sys.argv) > 1:
  if sys.argv[1] == 'cns':
    print 'Hello World!'
  elif sys.argv[1] == 'sfc':
    print 'Hello SFC!'
  else:
    print 'Hello',sys.argv[1]

