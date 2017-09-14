# coding:utf-8
import requests
from bs4 import BeautifulSoup
from pinyin import pinyin
response=requests.get("http://www.360doc.com/content/14/0327/16/8064468_364179892.shtml")
soup=BeautifulSoup(response.text)
data = BeautifulSoup.get_text(soup)
data2 = data.split('、')
list = [i for i in data2 if len(i)<20]
add = data2[21].split('\n')[-1]
add2 = add.split('：')
list.extend(add2)
list.append(data2[-1].split('\n')[0])
key = ['区', '县', '市', '\n']
list3 = [];list6 = []
for i in list:
    list5 = i.split('\n')
    list6.extend(list5)
for i in list6:
    list2 = [k for k in i]

    if '-' in list2:
        num = list2.index('-')
        del list2[:num+1]
    if '：' in list2:
        num = list2.index('：')
        del list2[:num + 1]
    for j in key:
        if j in list2:
            num = list2.index(j)
            del list2[num:]
    name = ''
    for l in list2:
        name = name + l
    list3.append(name)
list4 = [i for i in list3 if len(i)>=2]
citylist = list4[10:]
pinyinlist = []
for i in citylist:
    citypinyin = pinyin.get(i,format='strip',delimiter=' ').split()
    pinyinlist.append(citypinyin)
cityname = input('请输入城市名：')
lastcityname = pinyinlist[citylist.index(cityname)][-1]
for i in pinyinlist:
    if i[0] == lastcityname:
        print(citylist[pinyinlist.index(i)])
        lastcityname = i[-1]




