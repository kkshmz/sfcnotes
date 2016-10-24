import mechanize
import cookielib

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

# Want to debug messages?
br.set_debug_http(True)
br.set_debug_redirects(True)
br.set_debug_responses(True)

br.addheaders = [('User-agent', 'Mozilla/5.0 (X11; U; Linux i686; en-US; rv:1.9.0.1) Gecko/2008071615 Firefox/12.0')]


r = br.open("http://www.google.com/ncr")
html = r.read()
print html

print br.title()
print r.info()

for f in br.forms():
 print f

br.select_form(nr=0)

#Let's search
br.form['q'] = 'Keio SFC'
br.submit()
print br.response().read()


