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




year=2007
avgIVDP=[]
while(year<2017):
    tem = 0
    i = 1
    while(i<71):

        pkl_file = open('IVDP/IVDP_topic' + str(i) + '.pkl', 'rb')
        IVDPi = pickle.load(pkl_file)
        pkl_file.close()

        tem=tem+IVDPi[year-2007]
        i=i+1
    avg=tem/70

    avgIVDP.append(avg)
    year=year+1
    print(json.dumps(avgIVDP, encoding='UTF-8', ensure_ascii=False))

    output = open('均值vdp/IVDP.pkl', 'wb')
    pickle.dump(avgIVDP, output, -1)
    output.close()

year = 2007
avgRVDP = []

while (year < 2017):
    tem = 0
    i = 1
    while (i < 71):
        pkl_file = open('RVDP/RVDP_topic' + str(i) + '.pkl', 'rb')
        RVDPi = pickle.load(pkl_file)
        pkl_file.close()

        tem = tem + RVDPi[year - 2007]
        i = i + 1
    avg = tem / 70
    avgRVDP.append(avg)
    year = year + 1
    print(json.dumps(avgRVDP, encoding='UTF-8', ensure_ascii=False))

    output = open('均值vdp/RVDP.pkl', 'wb')
    pickle.dump(avgRVDP, output, -1)
    output.close()
