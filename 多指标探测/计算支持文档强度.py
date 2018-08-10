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

year=2005
while(year<2017):
    j=1
    while(j<13):
        month=0
        if j<10:
            month='0'+str(j)
        else:
            month=str(j)
        cursor = connect.cursor()
        sql = "select * from qiche70 WHERE pd like '"+str(year)+month+"%'"
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

            i=0
            while(i<70):
                if res[i+4]>0.1:   #支持文档
                    zhichidoc[i] = zhichidoc[i] + 1

                i=i+1

        output = open('zhichidocmonth/zhichidoc_'+str(year)+month+'.pkl', 'wb')
        pickle.dump(zhichidoc, output, -1)
        output.close()

        print(json.dumps(zhichidoc, encoding='UTF-8', ensure_ascii=False))
        j=j+1
    year=year+1

connect.close()
