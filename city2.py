#!/usr/bin/env python3
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
list3 = [];list6 = [];list7 = [];list9 = [];list8 = []

for i in list:

    list2 = [k for k in i]

    if '-' in list2:
        num = list2.index('-')
        del list2[:num+1]
    if '：' in list2:
        list7 = list2[:list2.index('：')]
        list2 = list2[list2.index('：')+1:]
        joinlist7 = ''.join(list7)
        list8 = [i.strip() for i in joinlist7.split('\n')]

        list11 = [m for m in list8[0]]
        for o in key:
                if o in list11:
                    num = list11.index(o)
                    del list11[num:]
        list12 = [n for n in list8[-1]]
        for o in key:
                if o in list12:
                    num = list12.index(o)
                    del list12[num:]
        list8 = [''.join(list11),''.join(list12)]
    for j in key:
        if j in list2:
            num = list2.index(j)
            del list2[num:]
    list3.append(''.join(list2))
    if list8 not in list9:
        list9.append(list8)
for i in list9:
    for j in i:
        list3.append(j)
list4 = [i for i in list3 if len(i)>=2 and len(i)<6]
citylist = list4[14:]
cityname = input('请输入城市名：')
def jielong(cityname,list):
    returncitylist = []
    pinyinlist = []
    for i in list:
        citypinyin = pinyin.get(i, format='strip', delimiter=' ').split()
        pinyinlist.append(citypinyin)
    pinyinname = pinyinlist[list.index(cityname)]
    lastcityname =pinyinname[-1]
    run = True
    while run:
        usedlist = []
        for j in pinyinlist:
            if j not in usedlist and j[0] == lastcityname and j != pinyinname:
                usedlist.append(j)
                returncitylist.append(list[pinyinlist.index(j)])
                lastcityname = j[-1]
            else:
                run = False

    return returncitylist
returncitylist = jielong(cityname,citylist)
print(returncitylist)