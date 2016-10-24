#!/usr/bin/env python
#-*- coding: utf-8 -*-

import json

a = open('ex-input-format1.json')
b = open('ex-input-format2.json')

aread =json.loads(a.read())
bread =json.loads(b.read())


#reading and printing a
for aitem in aread:
 title, name = aitem
 print name, title
 
#reading and printing b
for name,title in bread.iteritems():
	print name,title

a.close()
b.close()

#writing output file 
with open('example1-redumped.json', 'wb') as wf:
    json.dump(aread, wf)


