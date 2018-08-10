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


#求IVDP

i=1
while(i<71):

    pkl_file = open('IVI/IVI_topic'+str(i)+'.pkl', 'rb')
    topici = pickle.load(pkl_file)    #位置0是当前年份2005
    pkl_file.close()
    #print(json.dumps(topici, encoding='UTF-8', ensure_ascii=False))

    list_vdp=[]
    j = 2007  # 当前年份
    while(j<2017):
        m=2005     #算法循环参数
        VDP=0
        while(m<j):

            if topici[j-2005][m-2005+1]>y[m-2005+1] and topici[j-2005][m-2005]<y[m-2005]:
                YDP=m-2005-0.5
                VDP=(topici[j-2005][m-2005+1]+y[m-2005+1]+topici[j-2005][m-2005]+y[m-2005])/4
                break
            m=m+1
        j=j+1
        list_vdp.append(VDP)
    print(json.dumps(list_vdp, encoding='UTF-8', ensure_ascii=False))

    output = open('IVDP/IVDP_topic' + str(i) + '.pkl', 'wb')
    pickle.dump(list_vdp, output, -1)
    output.close()

    i=i+1


#求RVDP

i=1
while(i<71):

    pkl_file = open('RTI/RTI_topic'+str(i)+'.pkl', 'rb')
    topici = pickle.load(pkl_file)    #位置0是当前年份2005
    pkl_file.close()
    #print(json.dumps(topici, encoding='UTF-8', ensure_ascii=False))

    list_vdp=[]
    j = 2007  # 当前年份
    while(j<2017):
        m=2005     #算法循环参数
        VDP=0
        while(m<j):

            if topici[j-2005][m-2005+1]>y[m-2005+1] and topici[j-2005][m-2005]<y[m-2005]:
                YDP=m-2005-0.5
                VDP=(topici[j-2005][m-2005+1]+y[m-2005+1]+topici[j-2005][m-2005]+y[m-2005])/4
                break
            m=m+1
        j=j+1
        list_vdp.append(VDP)

    if (i==30):
        print 'qqqqq'

    print(json.dumps(list_vdp, encoding='UTF-8', ensure_ascii=False))

    output = open('RVDP/RVDP_topic' + str(i) + '.pkl', 'wb')
    pickle.dump(list_vdp, output, -1)
    output.close()

    i=i+1

