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
print '=======================================I V I================================='
i = 1
list=[]
list1=[]
while(i<71):

    pkl_file = open('IVI与基线的差/topic'+str(i)+'.pkl', 'rb')
    IVDPi = pickle.load(pkl_file)
    pkl_file.close()

    m=-1
    n=-1   #初始时m,n赋值
    j=0
    while(j<10):
        if m !=-1 and n!=-1:
            break
        elif IVDPi[j]<0 and m!=-1:
            n=j-0.5
        elif IVDPi[j]>0 and m==-1:
            m=j-0.5
        j=j+1
    list.append(m)
    list1.append(n)
    if m==-0.5:
        m='数据开始时间'
    elif m == -1:
        m = '未达到新兴阶段'
    else:
        m=m+2007
    if n == -1:
        n = '未达到成熟阶段'
    else:
        n=n+2007
    print '主题'+str(i)+'的新兴主题突破时间：'+str(m)+',结束时间：'+str(n)+'。'



    i = i + 1

output = open('突破时间/IVItopic.pkl', 'wb')
pickle.dump(list, output, -1)
output.close()
output = open('结束时间/IVItopic.pkl', 'wb')
pickle.dump(list1, output, -1)
output.close()

print(json.dumps(list, encoding='UTF-8', ensure_ascii=False))
print len(list)


print '========================================================================'

print '====================================R T I===================================='
i = 1
list=[]
list1=[]
while(i<71):

    pkl_file = open('RTI与基线的差/topic'+str(i)+'.pkl', 'rb')
    RVDPi = pickle.load(pkl_file)
    pkl_file.close()

    m=-1
    n=-1   #初始时m,n赋值
    j=0
    while(j<10):
        if m !=-1 and n!=-1:
            break
        elif RVDPi[j]<0 and m!=-1:
            n=j-0.5
        elif RVDPi[j]>0 and m==-1:
            m=j-0.5
        j=j+1

    list.append(m)
    list1.append(n)
    if m==-0.5:
        m='数据开始时间'
    elif m == -1:
        m = '未达到新兴阶段'
    else:
        m=m+2007
    if n == -1:
        n = '未达到成熟阶段'
    else:
        n=n+2007
    print '主题'+str(i)+'的新兴主题突破时间：'+str(m)+',结束时间：'+str(n)+'。'


    i = i + 1
output = open('突破时间/RTItopic.pkl', 'wb')
pickle.dump(list, output, -1)
output.close()
output = open('结束时间/RTItopic.pkl', 'wb')
pickle.dump(list1, output, -1)
output.close()
print '========================================================================'

print '===============================RTI和IVI结合========================================='
i = 1
list=[]
list1=[]
while(i<71):

    pkl_file = open('IVI与基线的差/topic'+str(i)+'.pkl', 'rb')
    IVDPi = pickle.load(pkl_file)
    pkl_file.close()
    pkl_file = open('RTI与基线的差/topic'+str(i)+'.pkl', 'rb')
    RVDPi = pickle.load(pkl_file)
    pkl_file.close()

    m=-1
    n=-1   #初始时m,n赋值
    j=0
    while(j<10):
        if m !=-1 and n!=-1:
            break
        elif IVDPi[j]<0 and RVDPi[j]<0 and m!=-1:
            n=j-0.5
        elif RVDPi[j]>0 and IVDPi[j]>0 and m==-1:
            m=j-0.5
        elif RVDPi[j]*IVDPi[j]<0 and m==-1:
            if j==9:
                break
            elif RVDPi[j]+IVDPi[j]>0 and RVDPi[j+1]+IVDPi[j+1]>0:
                m=j-0.5

        j=j+1
    list.append(m)
    list1.append(n)
    if m==-0.5:
        m='数据开始时间'
    elif m == -1:
        m = '未达到新兴阶段'
    else:
        m=m+2007
    if n == -1:
        n = '未达到成熟阶段'
    else:
        n=n+2007
    print '主题'+str(i)+'的新兴主题突破时间：'+str(m)+',结束时间：'+str(n)+'。'

    i = i + 1
output = open('突破时间/I+Rtopic.pkl', 'wb')
pickle.dump(list, output, -1)
output.close()
output = open('结束时间/I+Rtopic.pkl', 'wb')
pickle.dump(list1, output, -1)
output.close()


pkl_file = open('突破时间/IVItopic.pkl', 'rb')
tupo1 = pickle.load(pkl_file)
pkl_file.close()


pkl_file = open('突破时间/RTItopic.pkl', 'rb')
tupo2 = pickle.load(pkl_file)
pkl_file.close()

pkl_file = open('突破时间/I+Rtopic.pkl', 'rb')
tupo3 = pickle.load(pkl_file)
pkl_file.close()
pkl_file = open('结束时间/IVItopic.pkl', 'rb')
jieshu1 = pickle.load(pkl_file)
pkl_file.close()


pkl_file = open('结束时间/RTItopic.pkl', 'rb')
jieshu2 = pickle.load(pkl_file)
pkl_file.close()

pkl_file = open('结束时间/I+Rtopic.pkl', 'rb')
jieshu3 = pickle.load(pkl_file)
pkl_file.close()


i = 1

while(i<71):

    m=tupo1[i-1]
    n=jieshu1[i-1]
    print m,
    print '====',
    print n,
    if m==-0.5:
        m='数据开始时间'
    elif m == -1:
        m = '未达到新兴阶段'
    else:
        m=m+2007
    if n == -1:
        n = '未达到成熟阶段'
    else:
        n=n+2007
    print '主题'+str(i)+'的新兴主题IVI突破时间：'+str(m)+',结束时间：'+str(n)+'。',

    m = tupo2[i - 1]
    n=jieshu2[i-1]
    print m,
    print '====',
    print n,
    if m==-0.5:
        m='数据开始时间'
    elif m == -1:
        m = '未达到新兴阶段'
    else:
        m=m+2007
    if n == -1:
        n = '未达到成熟阶段'
    else:
        n=n+2007
    print '主题' + str(i) + '的新兴主题RTI突破时间：' + str(m) + ',结束时间：' + str(n) + '。',

    m = tupo3[i - 1]
    n=jieshu3[i-1]
    print m,
    print '====',
    print n,
    if m==-0.5:
        m='数据开始时间'
    elif m == -1:
        m = '未达到新兴阶段'
    else:
        m=m+2007
    if n == -1:
        n = '未达到成熟阶段'
    else:
        n=n+2007
    print '主题' + str(i) + '的新兴主题IVI结合RTI突破时间：' + str(m) + ',结束时间：' + str(n) + '。'

    i=i+1