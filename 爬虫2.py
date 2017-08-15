import requests
from bs4 import BeautifulSoup
response=requests.get("http://www.szsmb.gov.cn/Szsmb/search?cateid=7")
soup=BeautifulSoup(response.content)
print(soup)
for i in soup.findAll("a"):
 print(i)
