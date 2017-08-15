import requests
from bs4 import BeautifulSoup
import re
 
def getHttpUrl(graburl,tip):
    r = requests.get(graburl)
    soup = BeautifulSoup(r.content)
 
    a = soup.find_all('a')
    urlList = []
    for i in a:
        #匹配字符串
        try:
            url =  i.get('href')
            pattern = re.compile(tip) 
            match = pattern.search(url) 
 
            if match:                              
                urlList.append(i)
      
        except: 
            continue
 
    return urlList


urlList = getHttpUrl('http://www.szsmb.gov.cn/Szsmb/search?cateid=7','/Szsmb')
b="http://www.szsmb.gov.cn"
result=[]
for i in urlList[2:7]:
    t="%s%s\n"%(b,i)
    result.append(t)


link=open("最新通知.doc","a")
link.writelines("\n\n中小企业服务署\n\n")
link.writelines(result)
print(result)
link.close()
