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
            continue
 
    return urlList

def gettitle(graburl):
    r = requests.get(graburl)
    soup = BeautifulSoup(r.content)
    a = soup.find_all('a')
    titlelist=[]
    for i in a:
        #匹配字符串
        try:
            url =  i.get('href')
            pattern = re.compile(r'/notices') 
            match = pattern.search(url) 
 
            if match:
                titlelist.append(i)
          
        except:
            continue
 
    return titlelist

urlList = getHttpUrl('http://www.szsti.gov.cn/notices')
titlelist = gettitle('http://www.szsti.gov.cn/notices')
b="http://www.szsti.gov.cn"
urlresult=[]
titleresult=[]
for i in urlList[2:7]:
    t="%s%s\n"%(b,i)
    urlresult.append(t)
for j in titlelist[2:7]:
    titleresult.append(j)
print(titleresult)
print(urlresult)
link=open("最新通知.doc","w")
link.writelines(urlresult)
link.close()
