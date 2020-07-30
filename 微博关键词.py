from bs4 import BeautifulSoup
from urllib.request import urlopen
import re

url="https://s.weibo.com/top/summary?cate=realtimehot"
html=urlopen(url).read().decode('utf-8')
soup=BeautifulSoup(html,features='lxml')

information=soup.find_all('tr')
information=information[2:]
rank=[]
news=[]
zan_num=[]
for each in information:
    rank_temp=each.find('td',{'class':'td-01 ranktop'})#获取排名
    if each.find('a',{'target':'_blank'}) is None: #获取新闻
        news.append(each.find('a')['word'])
    else:
        news.append(each.find('a',{'target':'_blank'}).get_text())
    num=each.find('span')#获取新闻
    rank.append(rank_temp.get_text())
    zan_num.append(num.get_text())

print("{0:<10}\t{1:{3}<30}\t{2:{3}>11}".format('rank','name','num', chr(12288)))
for i in range(len(rank)):
    print("{0:<10}\t{1:{3}<30}\t{2:{3}>11}".format(rank[i],news[i],zan_num[i],chr(12288)))