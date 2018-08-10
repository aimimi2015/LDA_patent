# coding: utf-8
import csv
import json
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


listABC=[1,2]
output = open('listABC.pkl', 'wb')
pickle.dump(listABC, output, -1)
output.close()


pkl_file = open('listABC.pkl', 'rb')
listABC = pickle.load(pkl_file)
print listABC[1]
print(json.dumps(listABC, encoding='UTF-8', ensure_ascii=False))
pkl_file.close()