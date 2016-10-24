#!/usr/bin/env python
#-*- coding: utf-8 -*-

import json

#Read all (5)  example input  files

a = open('ex-input-format1.json')
b = open('ex-input-format2.json')
c = open('ex-input-format3.json')
d = open('ex-input-format4.json')
e = open('ex-input-format5.json')

aread =json.loads(a.read())
bread =json.loads(b.read())
cread =json.loads(c.read())
dread =json.loads(d.read())
eread =json.loads(e.read())

#reading and printing a
for aitem in aread:
 title, name = aitem
 print name, title
#reading and printing b
for name,title in bread.iteritems():
	print name,title
#reading and printing c
for data1,data2 in cread.iteritems():
	print data1,data2

#Print/output “Cute Captain Tottoro” using values extracted from each of them.”Cute” from example 2, “Captain” from example 3, “Tottoro” from example 1

print bread["Tottoro"],cread["military"][0]["rank"],aread[2][1]

#Combine example 4 and 5
combined=dread+eread

a.close()
b.close()
c.close()
d.close()
e.close()

#save it as “combined45.json”
with open('combined45.json', 'wb') as wf:
    json.dump(combined, wf)


