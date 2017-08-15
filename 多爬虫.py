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

urlList = getHttpUrl('http://www.szsti.gov.cn/notices',"/notices")
b="http://www.szsti.gov.cn"
result=[]
for i in urlList[2:7]:       
    t="%s%s\n"%(b,i)
    result.append(t)

link=open("最新通知.doc","w")
link.writelines("\n\n科创委\n\n")
link=open("最新通知.doc","a")
link.writelines(result)

urlList = getHttpUrl('http://www.szsmb.gov.cn/Szsmb/search?cateid=7','/Szsmb')
b="http://www.szsmb.gov.cn"
result=[]
for i in urlList[2:7]:
    t="%s%s\n"%(b,i)
    result.append(t)

link=open("最新通知.doc","a")
link.writelines("\n\n中小企业服务署\n\n")
link.writelines(result)

urlList = getHttpUrl('http://www.szft.gov.cn/bmxx/qkjj/tzgg/','./')
b="http://www.szft.gov.cn/bmxx/qkjj/tzgg"
result=[]
for i in urlList[7:12]:
    t="%s%s\n"%(b,i)
    result.append(t)

link=open("最新通知.doc","a")
link.writelines("\n\n\n福田科创委\n\n")
link.writelines(result)

urlList = getHttpUrl('http://zjsq.szft.gov.cn/newsite/pzlaw_list.action?type=1','/newsite')
b="http://zjsq.szft.gov.cn"
result=[]
for i in urlList[1:6]:
    t="%s%s\n"%(b,i)
    result.append(t)
  
link=open("最新通知.doc","a")
link.writelines("\n\n福田产业资金网\n\n")
link.writelines(result)

urlList = getHttpUrl('http://www.szlh.gov.cn/icatalog/98/B204/09/09-01/09-01-\
01/index.shtml','/icatalog')
b="http://www.szlh.gov.cn"
result=[]
for i in urlList[27:32]:
    t="%s%s\n"%(b,i)
    result.append(t)

link=open("最新通知.doc","a")
link.writelines("\n\n罗湖科创局\n\n")
link.writelines(result)

urlList = getHttpUrl('http://bast.baoan.gov.cn/gzdt/tzgg/','./')
b="http://bast.baoan.gov.cn/gzdt/tzgg"
result=[]
for i in urlList[33:38]:
    t="%s%s\n"%(b,i)
    result.append(t)

link=open("最新通知.doc","a")
link.writelines("\n\n宝安科创局\n\n")
link.writelines(result)

urlList = getHttpUrl('http://jfj.szlhxq.gov.cn/lhjjfwj/zhxx34/ggtz/index.html',\
'/lhjjfwj')
b="http://jfj.szlhxq.gov.cn"
result=[]
for i in urlList[23:28]:
    t="%s%s\n"%(b,i)
    result.append(t)

link=open("最新通知.doc","a")
link.writelines("\n\n龙华经济促进局\n\n")
link.writelines(result)


link.close()
