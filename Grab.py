# -*- coding: gb2312 -*-
from urllib import urlopen
import re
import sqlite3
import time
time1 = time.localtime()
p = re.compile('<h4><a href="/article/\d{5}/1.html" target="_blank">.{0,100}</a></h4>')#ƥ������������ַ
s = re.compile('<meta name="description".{0,1000}>')#ƥ�����������ڵ����

titlere = re.compile('">.{2,100}</a')#ƥ�����
urlre = re.compile('/article/\d{5}/1.html')#ƥ��������ַ
contentre = re.compile('content=".{0,1000}"')#ƥ��������
contentre1 = re.compile('".{0,1000}"')
urlpath = 'http://www.huxiu.com'
text = urlopen(urlpath).read()
   #�������ݿ�
hwbDB = sqlite3.connect("huxiu.db")
   #�����α�
cu = hwbDB.cursor()
   #������(���������ɾ�����ڴ���һ���µ�)
hwbDB.execute('drop table if exists huxiulog')
cu.execute("create table  huxiulog(id integer primary key,title text,content text)")
  
for sp in p.findall(text):
  title = titlere.search(sp).group(0).replace('"','')
  #print title
  content = urlre.search(sp).group(0).replace('"','')
 
  url = urlpath + content
  page = urlopen(url).read()
 
  str = s.search(page).group()
  context = contentre.search(str).group().replace('"','')
  cu.execute('insert into huxiulog values (NULL, "%s", "%s")' %((title),(context)))


hwbDB.commit()
cu.close()
hwbDB.close()
time2 = time.localtime()
time3 = time2.tm_min-time1.tm_min
if time3==0:
     print "1��������ʱ�䣺%s" %(time2.tm_sec-time1.tm_sec)
else:
     print "2��������ʱ�䣺%s" %(time2.tm_sec+60-time1.tm_sec)
print "ץȡ���"
print "��������ʱ�䣺%s" %time.clock()
time.sleep(5)
