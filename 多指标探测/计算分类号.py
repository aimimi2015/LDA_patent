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

i=1
while(i<71):
    if (i==30):
        print ('i=30')   #打印示例主题
    dict = {}  # 一年一个大字典，用相邻年减去为每年的分类号数
    list_num=[]  #存的是字典长度
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
        #RTIdoc = [0,0,0,0,0,0,0,0,0,0,0,0]

        for res in results:
            #print res[0],res[1],res[2],res[3],res[4],res[5]
            #list1 = []  # 这就是个临时的，共51长，接受分类号和主题概率
            #list1.append(res[2])  #存的是分类号，存到了list1的第0位

                            #先搞个临时的，然后通过存成不同名字实现zhichidoc2005的2005命名


               #支持文档

            if res[i+3]>0.1:
                tem=res[2]
                num = tem.index('/')
                tem=tem[0:num+3]
                dict[tem]=1
                #print tem
                    #RTIdoc[i - 1] = RTIdoc [i - 1] + 1    #这里从0开始
        list_num.append(len(dict))
        #print len(dict)

        #print(json.dumps(list_num, encoding='UTF-8', ensure_ascii=False))

        year = year + 1
    output = open('RTIdoc/RTIdoc_topic' + str(i) + '.pkl', 'wb')
    pickle.dump(list_num, output, -1)
    output.close()
    print(json.dumps(list_num, encoding='UTF-8', ensure_ascii=False))
    i = i + 1

connect.close()

