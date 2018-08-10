# coding: utf-8
import csv
import sys
import jieba, os
import re
from gensim import corpora, models, similarities
import logging
import jieba.posseg
import time
import string
import json
import pickle
import pprint


pkl_file = open('topiclist.pkl', 'rb')

topiclist = pickle.load(pkl_file)


print(json.dumps(topiclist, encoding='UTF-8', ensure_ascii=False))

print topiclist[1]

pkl_file.close()