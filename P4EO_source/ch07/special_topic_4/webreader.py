##
#  This program prints all addresses contained in a web page that 
#  references to other web sites.

from urllib.request import urlopen

address = "http://horstmann.com/index.html"
webPage = urlopen(address)

encoding = "utf-8"
for line in webPage :
   line = str(line, encoding)
   key = 'href="http://'
   if key in line :
      start = line.index(key) + len(key)
      last = line.index('"', start)
      print(line[start : last])
      
webPage.close()
