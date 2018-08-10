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
import matplotlib.pyplot as plt
from scipy.optimize import curve_fit
import numpy as np
#新颖度曲线

#用指数形式来拟合
x = np.linspace(0, 11, 12)

def func(x):
    return np.math.pow(0.85, x)

y = []
i=0
while i<12:
    y.append(func(x[i]))
    i=i+1

i=1
while(i<71):
    year = 2005
    topici_year = []
    while (year < 2017):

        pkl_file = open('zhichidoc/zhichidoc_'+str(year)+'.pkl', 'rb')
        topici = pickle.load(pkl_file)   #从0开始的列表，存的是该年50个主题的支持文档
        pkl_file.close()

        #先求IVI。

        topici_year.append(topici[i-1])  #把某个主题的历年的支持文档放到

        year=year+1
    print(json.dumps(topici_year, encoding='UTF-8', ensure_ascii=False))



#####计算每个主题的12年支持文档强度
    print 'topic'+str(i)
    #print(json.dumps(topici_year, encoding='UTF-8', ensure_ascii=False))
    sum=topici_year[0]+topici_year[1]+topici_year[2]+topici_year[3]+topici_year[4]+topici_year[5]+topici_year[6]+topici_year[7]+topici_year[8]+topici_year[9]+topici_year[10]+topici_year[11]
    print sum

    #开始计算ivi
    list_ivi=[]    #里面存的是2005年为当前年份、2006位当前、。。。。、2016.。。。每个里面又存了2005-2005、2005-2006。。

    j=2005
    while (j < 2017):
        x=j-2005
        totol=topici_year[0]
        while(x>0):    #求totol
            totol=totol+topici_year[x]  #第一个加最后一个
            x=x-1
        totol=float(totol)

        list = []
        m = j - 2004  # 求一共有几个IVI
        n = m
        p = 1
        tem = topici_year[0]
        list.append(tem / totol)
        while (n > 1):
            tem = tem + topici_year[p]
            list.append(tem / totol)

            p = p + 1
            n = n - 1
        j = j + 1
        print(json.dumps(list, encoding='UTF-8', ensure_ascii=False))
        list_ivi.append(list)
    if (i == 30):
        print ('30303030')
    print(json.dumps(list_ivi, encoding='UTF-8', ensure_ascii=False))

    output = open('IVI/IVI_topic'+str(i)+'.pkl', 'wb')
    pickle.dump(list_ivi, output, -1)
    output.close()

    i=i+1