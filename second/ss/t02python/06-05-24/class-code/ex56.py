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


r = br.open("http://www.utexas.edu/world/univ/alpha/")
html = r.read()
soup = bsoup(html)

universities = soup.findAll('a',{'class':'institution'})

#print universities
#print universities[2]


for eachuniversity in universities:
#  print eachuniversity['href']+","+eachuniversity.string
   print eachuniversity.string
   #print eachuniversity

