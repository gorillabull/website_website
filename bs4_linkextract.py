 
import urllib2 as ul3 

from bs4 import BeautifulSoup as bs 

page = ul3.urlopen('https://rezi.io')
soup = bs(page, features="lxml")


srcs =soup.find_all('script')
 
for s in srcs:
    print(s.get('src'))

print(soup.head)