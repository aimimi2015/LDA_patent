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

i = 1
while(i<71):

    pkl_file = open('IVDP/IVDP_topic' + str(i) + '.pkl', 'rb')
    IVDPi = pickle.load(pkl_file)
    #print(json.dumps(IVDPi, encoding='UTF-8', ensure_ascii=False))

    pkl_file.close()

    pkl_file = open('均值vdp/IVDP.pkl', 'rb')
    augIVDP = pickle.load(pkl_file)
    #print(json.dumps(augIVDP, encoding='UTF-8', ensure_ascii=False))

    pkl_file.close()


    j=0
    list=[]
    while(j<10):

        VDPcha=IVDPi[j]-augIVDP[j]
        j=j+1
        list.append(VDPcha)
    #print(json.dumps(list, encoding='UTF-8', ensure_ascii=False))

    if i == 1:
        print ' '
        print 'topic1'
        print ' '
    if i == 14:
        print ' '
        print 'topic14'
        print ' '
    if i == 27:
        print ' '
        print 'topic27'
        print ' '
    if i == 28:
        print ' '
        print 'topic28'
        print ' '
    if i == 42:
        print ' '
        print 'topic42'
        print ' '
    if i == 44:
        print ' '
        print 'topic44'
        print ' '
    if i == 51:
        print ' '
        print 'topic51'
        print ' '
    if i == 52:
        print ' '
        print 'topic52'
        print ' '
    if i == 66:
        print ' '
        print 'topic62'
        print ' '

    print(json.dumps(list, encoding='UTF-8', ensure_ascii=False))
    output = open('IVI与基线的差/topic'+str(i)+'.pkl', 'wb')
    pickle.dump(list, output, -1)
    output.close()
    i=i+1
print '==========================='

i = 1
while(i<71):


    pkl_file = open('RVDP/RVDP_topic' + str(i) + '.pkl', 'rb')
    RVDPi = pickle.load(pkl_file)
    #if (i == 30):
        #print(json.dumps(RVDPi, encoding='UTF-8', ensure_ascii=False))

    pkl_file.close()

    pkl_file = open('均值vdp/RVDP.pkl', 'rb')
    augRVDP = pickle.load(pkl_file)
    #if (i == 30):
        #print(json.dumps(augRVDP, encoding='UTF-8', ensure_ascii=False))
    pkl_file.close()


    j=0
    list=[]
    while(j<10):

        VDPcha=RVDPi[j]-augRVDP[j]
        j=j+1
        list.append(VDPcha)
    #print(json.dumps(list, encoding='UTF-8', ensure_ascii=False))

    if i == 8:
        print ' '
        print 'topic8'
        print ' '
    if i == 14:
        print ' '
        print 'topic14'
        print ' '
    if i == 27:
        print ' '
        print 'topic27'
        print ' '
    if i == 28:
        print ' '
        print 'topic28'
        print ' '
    if i == 42:
        print ' '
        print 'topic42'
        print ' '
    if i == 44:
        print ' '
        print 'topic44'
        print ' '
    if i == 51:
        print ' '
        print 'topic51'
        print ' '
    if i == 52:
        print ' '
        print 'topic52'
        print ' '
    if i == 66:
        print ' '
        print 'topic62'
        print ' '
    print(json.dumps(list, encoding='UTF-8', ensure_ascii=False))
    output = open('RTI与基线的差/topic'+str(i)+'.pkl', 'wb')

    pickle.dump(list, output, -1)
    output.close()
    i=i+1
print '==========================='
print ' '

print ' '

i = 1
while(i<71):

    pkl_file = open('IVDP/IVDP_topic' + str(i) + '.pkl', 'rb')
    IVDPi = pickle.load(pkl_file)
    pkl_file.close()

    pkl_file = open('均值vdp/IVDP.pkl', 'rb')
    augIVDP = pickle.load(pkl_file)
    pkl_file.close()

    pkl_file = open('均值vdp/RVDP.pkl', 'rb')
    augRVDP = pickle.load(pkl_file)
    pkl_file.close()

    pkl_file = open('RVDP/RVDP_topic' + str(i) + '.pkl', 'rb')
    RVDPi = pickle.load(pkl_file)
    pkl_file.close()

    j=0
    list=[]
    while(j<10):

        VDPcha=IVDPi[j]+RVDPi[j]-augIVDP[j]-augRVDP[j]
        j=j+1
        list.append(VDPcha)
    #print(json.dumps(list, encoding='UTF-8', ensure_ascii=False))

    if i == 8:
        print ' '
        print 'topic8'
        print ' '
    if i == 14:
        print ' '
        print 'topic14'
        print ' '
    if i == 27:
        print ' '
        print 'topic27'
        print ' '
    if i == 28:
        print ' '
        print 'topic28'
        print ' '
    if i == 42:
        print ' '
        print 'topic42'
        print ' '
    if i == 44:
        print ' '
        print 'topic44'
        print ' '
    if i == 51:
        print ' '
        print 'topic51'
        print ' '
    if i == 52:
        print ' '
        print 'topic52'
        print ' '
    if i == 66:
        print ' '
        print 'topic62'
        print ' '

    print(json.dumps(list, encoding='UTF-8', ensure_ascii=False))
    output = open('IVI与RTI整体与基线的差/topic'+str(i)+'.pkl', 'wb')
    pickle.dump(list, output, -1)
    output.close()
    i=i+1