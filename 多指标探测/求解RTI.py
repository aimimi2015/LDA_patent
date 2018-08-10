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


    pkl_file = open('RTIdoc/RTIdoc_topic'+str(i)+'.pkl', 'rb')
    topici = pickle.load(pkl_file)   #从0开始的列表，存的是该年50个主题的支持文档
    pkl_file.close()

    #先求IVI。


    print(json.dumps(topici, encoding='UTF-8', ensure_ascii=False))

    #开始计算ivi
    list_rti=[]    #里面存的是2005年为当前年份、2006位当前、。。。。、2016.。。。每个里面又存了2005-2005、2005-2006。。

    j=2005
    while (j < 2017):
        x=j-2005
        totol=topici[j-2005]
        totol=float(totol)

        list = []
        m = j - 2004  #
        n = 1

        list.append(topici[0] / totol)
        while (n <m):
            list.append(topici[n] / totol)
            n = n +1
        j = j + 1
        print(json.dumps(list, encoding='UTF-8', ensure_ascii=False))
        list_rti.append(list)
    if(i==30):
        print ('30303030')
    print(json.dumps(list_rti, encoding='UTF-8', ensure_ascii=False))

    output = open('RTI/RTI_topic'+str(i)+'.pkl', 'wb')
    pickle.dump(list_rti, output, -1)
    output.close()

    i=i+1