# coding: utf-8
import csv
import sys
import jieba, os
import time
from gensim import corpora, models, similarities
import numpy as np
import logging
import jieba.posseg
from compiler.ast import flatten
from gensim.models import basemodel
import pymysql
import pickle
import json

n = 1
h=0
# 创建连接
connect = pymysql.connect(host='localhost',
                          port=3306, user='root',
                          passwd='123456',
                          db='test2',
                          charset='utf8')
# 获取游标

zhichidoczongshu = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,
             0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
year=2005
while(year<2017):
    cursor = connect.cursor()
    sql = "select * from qiche70 WHERE pd like '"+str(year)+"%'"
    #sql1="select * from qiche WHERE pd like '2005'"
    #print sql

    cursor.execute(sql)
    connect.commit()
    results = cursor.fetchall()

    cursor.close()
    zhichidoc = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,
                 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,0, 0, 0, 0, 0, 0, 0, 0, 0, 0,0, 0, 0, 0, 0, 0, 0, 0, 0, 0]



    for res in results:
        #print res[0],res[1],res[2],res[3],res[4],res[5]
        list1 = []  # 这就是个临时的，共51长，接受分类号和主题概率
        list1.append(res[2])  #存的是分类号，存到了list1的第0位

                        #先搞个临时的，然后通过存成不同名字实现zhichidoc2005的2005命名
        i=1
        while(i<71):

            if res[i+3]<=0.1:   #支持文档
                list1.append(0)
            else:
                list1.append(1)

                zhichidoc[i - 1] = zhichidoc[i - 1] + 1    #这里从0开始
                zhichidoczongshu[i-1]=zhichidoczongshu[i-1]+1

            i=i+1

        output = open('zhichidoc/zhichidoc_'+str(year)+'.pkl', 'wb')
        pickle.dump(zhichidoc, output, -1)
        output.close()

    print(json.dumps(zhichidoc, encoding='UTF-8', ensure_ascii=False))
    print (zhichidoc[29])
    print (zhichidoczongshu[29])
    year=year+1

connect.close()

print(json.dumps(zhichidoczongshu, encoding='UTF-8', ensure_ascii=False))

output = open('zhichidoc.pkl', 'wb')
pickle.dump(zhichidoczongshu, output, -1)
output.close()
