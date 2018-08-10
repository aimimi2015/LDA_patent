# coding: utf-8
import csv
import sys
import jieba, os
import re

import pymysql
from gensim import corpora, models, similarities
import logging
import jieba.posseg
import time
import string
import json
import pickle
import pprint
import matplotlib.pyplot as plt
import numpy as np
import json
import pickle

T = 80   #主题数

lda = models.LdaModel.load('qiche/'+str(T)+'/mylda_quanguo.pkl')  # LDA模型

list1 = []
list2=[]
topiclist = []

delEStr = string.punctuation + ' ' + string.digits  # ASCII 标点符号，空格和数字  要删除的
identify = string.maketrans('', '')
delCStr = '《》（）&%￥#@！{}【】'
i=110

for j in range(0, T):
    # print(lda.print_topic(j, topn=5))
    # print lda.print_topic(j, topn=20)

    a=lda.print_topic(j,topn=i).encode("utf-8")

    x=0
    while (x<i):
        list1=a.split('+')
        list2=list1[x].split('*')
        # list2[1]=list2[1].strip('"')
        # list2[1] = list2[1].strip('"')
        list2[1] = eval(list2[1])
        #print list2[1]
        topiclist.append(list2[1])
        topiclist.append(list2[0])
        x=x+1
print(json.dumps(topiclist, encoding='UTF-8', ensure_ascii=False))
f = open("qiche/"+str(T)+".txt", 'w')

for k in range(0,T):
    m=i*k*2
    print k
    for j in range(m, m+2*i):
        f.write(topiclist[j].strip())
        if(j!=m+2*i-1):
            f.write(" ")
    if(k!=T-1):
        f.write('\n')


# print topiclist[1]
# print len(topiclist)
# print j
# for i in range(10):
#  topic2[i]

