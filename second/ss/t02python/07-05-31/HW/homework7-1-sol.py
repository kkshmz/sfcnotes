#!/usr/bin/env python
import mechanize
import cookielib
#from BeautifulSoup import BeautifulSoup as bsoup
from bs4 import BeautifulSoup as bsoup
br = mechanize.Browser()

import re

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

r = br.open("http://www.jma.go.jp/en/yoho/320.html")
html = r.read()
#soup = bsoup(html)
soup = bsoup(html,'html.parser')

weathers = soup.findAll('td',{'class':'info'})
#print weathers

#Will get 6 items [0-5],Tomorrow's weather is item number[1] or [4] (same content)
#print weathers[1]

weather=str(weathers[1])

#print weather

match = re.findall(r'([A-Zw,.-]+)',weather)
print match
