import requests
from bs4 import BeautifulSoup
response=requests.get("http://www.szsti.gov.cn/notices")
soup=BeautifulSoup(response.text)
for i in soup.find_all('div'):
    one = i.find_all('a')
    two = i.find_all('li')
    printnt ("%s %s" % (one,two))
