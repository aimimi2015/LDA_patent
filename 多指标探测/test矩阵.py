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

lda = models.LdaModel.load('../tem/mylda_飞行航空.pkl') #LDA模型

topic1=[]
topic2=[]
topic3=[]
list1=[]
topiclist=[]

delEStr = string.punctuation + ' ' + string.digits  #ASCII 标点符号，空格和数字  要删除的
identify = string.maketrans('','')
delCStr = '《》（）&%￥#@！{}【】'

topiclist2=[]
for j in range(0, 3):
    #print(lda.print_topic(j, topn=5))
    print lda.print_topic(j, topn=20)
    num = j
    #topic1 = []
    topic2 = []
    topic3 = []
    #print num
    topic1.append(lda.print_topic(num).encode("utf-8"))    #topic1装的是每个未经处理的行主题，不是一共有j行，这里旧村50个，为了以后好取
    list1 = topic1[j].split('+')     #把当前行主题用加号分开，原来的列表中的一个元素是一行字符串，现在变成一个用加号分开的列表

    #print(json.dumps(list1, encoding='UTF-8', ensure_ascii=False))
    i=0    #是指的刚才那个主题词，之前存的lda是一行10个主题词，所以i<10

    while i<10:
        s=list1[i]
        s1 = s.translate(identify, delEStr)  # 去掉ASCII 标点符号和空格数字  identify翻译表，翻译表是通过maketrans方法转换而来。delEStr是一个包含英文标点符号和数字的字符串，就如 '(){}<>1234 ' 这样。delCStr是一个包含中文标点符号的字符串。s是一个测试字符串。
        topic2.append(s1)

            #if re.findall('[\x80-\xff].', s):  # s为中文
            #    s = s.translate(identify, delCStr)
            #    topic2[i]=s
            #else:  # s为英文
            #    topic2[i] = s


        s2 = list1[i]
        s3 = filter(lambda ch: ch in '0123456789.', s2)  # 去掉ASCII 汉字 identify翻译表，翻译表是通过maketrans方法转换而来。
        topic3.append(s3)

        i = i + 1

    topic=dict(zip(topic2, topic3))
        #print topic





    print('==================================================================================')
    print(json.dumps(topic2, encoding='UTF-8', ensure_ascii=False))
    print('==================================================================================')
    print(json.dumps(topic3, encoding='UTF-8', ensure_ascii=False))
    print('==================================================================================')
    print(json.dumps(topic, encoding='UTF-8', ensure_ascii=False))
    print('==================================================================================')
    topiclist.append(topic)

    #topiclist2.append(topiclist)

print('==========================================================================================')
    #print topic['答']
    #print(json.dumps(topiclist, encoding='UTF-8', ensure_ascii=False))

print(json.dumps(topiclist, encoding='UTF-8', ensure_ascii=False))

print topiclist[1]
#for i in range(10):
          #  topic2[i]


'''
遍历字典
1 for (d,x) in dict.items():
2     print "key:"+d+",value:"+str(x)
3
4 for d,x in dict.items():
5     print "key:"+d+",value:"+str(x)
'''


output = open('topiclist.pkl', 'wb')
# Pickle the list using the highest protocol available.
pickle.dump(topiclist, output, -1)
output.close()