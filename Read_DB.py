# -*- coding: gb2312 -*-
import sqlite3
import time
DB = sqlite3.connect("huxiu.db")
cu = DB.cursor()
cu.execute("select * from huxiulog")
print "开始"
for line in cu.fetchall():
  for f in line:
      print f,'\n',
  print
print "结束"

