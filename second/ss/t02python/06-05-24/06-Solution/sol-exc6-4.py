#!/usr/bin/env python
#-*- coding: utf-8 -*-
import re
import mechanize
import cookielib
from BeautifulSoup import BeautifulSoup as bsoup
br = mechanize.Browser()

# cookie jar
cj = cookielib.LWPCookieJar()
br.set_cookiejar(cj)

br.set_handle_equiv(True)
#br.set_handle_gzip(True)
br.set_handle_redirect(True)
br.set_handle_referer(True)
br.set_handle_robots(False)
br.set_handle_refresh(mechanize._http.HTTPRefreshProcessor(), max_time=1)

br.addheaders = [('User-agent', 'Mozilla/5.0 (X11; U; Linux i686; en-US; rv:1.9.0.1) Gecko/2008071615 Firefox/12.0')]

#Yes i know some of you have probably tried this one:
#r = br.open("http://en.wikipedia.org/wiki/List_of_universities_in_Japan")
#It's possible but more challenging/tricky

#This one is easier instead (you are free to decide any website as per the instruction)
r = br.open("http://www.asahi-net.or.jp/~tc9w-ball/useful/Juniversities.htm")

html = r.read()
soup = bsoup(html)

#Have a look at the manual (which is the point of this exercise)
#http://www.crummy.com/software/BeautifulSoup/bs3/documentation.html#The basic find method: findAll(name, attrs, recursive, text, limit, **kwargs)

#This will find all <td> tags which has no atttribute
universities=soup.findAll(lambda tag: tag.name == 'td' and not tag.attrs)
#print universities, you can try to print it first
# you'll find out that there are <td> tags that contains <a> tags with href links which are not the ones that you want.


#open the file to keep the list, as required
fo = open('japanuniv.txt', 'w')

for eachuniversity in universities:
#.next method navigate to the "next", i.e inner side of the <td>tags
# you will get : University Name, and also the a> tags with href links
   t=eachuniversity.next
   #print type(t) you can try to check the types of those and found out that th ones that you want
   #(University name) is the one with type <class 'BeautifulSoup.Tag'>
   #Let's filter it here
   if (str(type(t)) != "<class 'BeautifulSoup.Tag'>"):
      
      print t.string
      fo.write( t.string+"\n")
   
# Close the file
fo.close()
   
