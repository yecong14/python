import requests
from bs4 import BeautifulSoup
import re
 
def getHttpUrl(graburl):
    r = requests.get(graburl)
    soup = BeautifulSoup(r.content)
 
    a = soup.find_all('a')
    urlList = []
    for i in a:
        #匹配字符串
        try:
            url =  i.get('href')
            pattern = re.compile(r'/notices') 
            match = pattern.search(url) 
 
            if match:
                urlList.append(url)
        except:
            print("error")
 
    return urlList

urlList = getHttpUrl('http://www.szsti.gov.cn/notices')
for i in urlList:
    print (i)

