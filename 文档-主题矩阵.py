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

jieba.load_userdict("dic/mydic.txt")
jieba.load_userdict("dic/baidu.txt")
jieba.load_userdict("dic/专利发明词条.txt")
jieba.load_userdict("dic/机械工程词汇大全.txt")
jieba.load_userdict("dic/材料科学与工程.txt")
jieba.load_userdict("dic/航天航空专业术语.txt")
jieba.load_userdict("dic/船舶工程名词.txt")



stopwords = {}.fromkeys([line.rstrip() for line in open('stopword.txt')])   #fromkeys该方法用于重建一个字典
cipinstop = {}.fromkeys([line.rstrip() for line in open('cipinstop.txt')])

print('读取停用词，停用词频完成')
print(time.strftime('%Y-%m-%d %H:%M:%S',time.localtime(time.time())))
print('='*30)

rode =[]
num=0
arr2 = np.array([])
a = np.array([])
#scvtest/飞行航空
walk = os.walk('patent')
for root, dirs, files in walk:
    for name in files:
        str1 = os.path.join(root, name)
        str3 = 'DS_Store'
        numDS = str1.count(str3)
        if numDS == 0:
            rode.append(os.path.join(root, name))

while num<len(rode):
    filename = rode[num]
    csvfile = open(filename, 'rb')
    reader = csv.reader(csvfile)
    for line in reader:
        arr = []
        if line[10]=='':
            continue
        str3 = line[3]
        str1 = str3[0:4]
        str2 = int(str1)

        list1 = list(line[1])
        if line[1]=='':
            continue

        if len(list1) < 7:
            continue
        if str2<2004:
            continue
        if line[16] == '':
            #print '到17'
            continue
        if line[15] == '':
            #print '到15'
            continue

        str = line[16]
        str15 = line[15]
        if list1[6] != '1':
            continue
        if str15 =='河北(13)':
            segs = list(jieba.cut(str, cut_all=True))
            final = []

            for seg in segs:
                seg = seg.encode('utf-8')
                seg = seg.strip()  # seg的格式是字符串，该函数可以去除字符串的空格,详见25-36行
                if seg not in stopwords:  # 结果和做了词性删除一样。
                    final.append(seg)

            new = "".join(final)

            dic = corpora.Dictionary.load('tem/河北/dict_河北.dict')
            corpus = dic.doc2bow(jieba.cut(new, cut_all=False))

            lda = models.LdaModel.load('tem/河北/mylda_河北.pkl')  # LDA模型

            for i in lda.get_document_topics(corpus):
                arr.append(i)

            arr = np.array(arr)
            arr = np.delete(arr, 0, axis=1)  # 从0开始删，或者[1,9]删除1到9个，删除列就是1维度，删除行是0维度 把标着主题号的那一列删除，变成一列，然后下面转换成一行
            arr.shape = 1, -1

            arr = flatten(arr)  # 变成列表了
            arr = np.array(arr[0])

            if arr2.shape == (0,):
                arr2 = arr
                continue
            else:
                arr2 = np.vstack((arr2, arr))
                continue
        else:
            continue

    csvfile.close()
    num=num+1
    print('完成一个csv文件')
    print(time.strftime('%Y-%m-%d %H:%M:%S',time.localtime(time.time())))
    print('='*30)

np.save("tem/河北/hebei2.npy",arr2)

#利用这种方法，保存文件的后缀名字一定会被置为.npy，这种格式最好只用
#numpy.load("filename")来读取。

np.savetxt("tem/河北/hebei2.txt",arr2)
#b =  numpy.loadtxt("filename.txt")
#用于处理一维和二维数组

print(arr2.shape)
print(arr2)