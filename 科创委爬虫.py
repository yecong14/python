import requests
from bs4 import BeautifulSoup
import re
 
def getHttpUrl(graburl):
    r = requests.get(graburl)
    soup = BeautifulSoup(r.content)
 
    a = soup.find_all('a')
    urlList = []
    titlelist=[]
    for i in a:
        #匹配字符串
        try:
            url =  i.get('href')
            pattern = re.compile(r'/notices') 
            match = pattern.search(url) 
 
            if match:                              
                urlList.append(i)
                
        except:
            continue
 
    return urlList

urlList = getHttpUrl('http://www.szsti.gov.cn/notices')
b="http://www.szsti.gov.cn"
result=[]
for i in urlList[2:7]:       
    t="%s%s\n"%(b,i)
    result.append(t)
print(result)   
link=open("最新通知.doc","w")
link.writelines(result)
link.close()
