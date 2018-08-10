# coding: utf-8
import csv
import sys
import jieba, os
from gensim import corpora, models, similarities
import numpy as np
import logging
import jieba.posseg
from gensim.models import basemodel
from compiler.ast import flatten




train_set1 = []

stopwords = {}.fromkeys([line.rstrip() for line in open('linux/停用词.txt')])
cipinstop = {}.fromkeys([line.rstrip() for line in open('cipinstop.txt')])

f = open('./testpat.txt', 'r')
raw = f.read()
segs = list(jieba.cut(raw, cut_all=False))

final = []
for seg in segs:
    seg = seg.encode('utf-8')
    seg = seg.strip()  #seg的格式是字符串，该函数可以去除字符串的空格,详见25-36行
    words = jieba.posseg.cut(seg)
    for w in words:
        if w.flag.encode("utf-8") not in cipinstop:  # w.flag是w的词性    cipinstop是删除词性的
            break
        if seg in stopwords:
            break
        final.append(seg)
    #if seg not in stopwords:   #结果和做了词性删除一样。
        #final.append(seg)

new = "".join(final)

print(new)


dic = corpora.Dictionary.load('主题词转换txt/qiche/70/dict_qiche.dict')
corpus = dic.doc2bow(jieba.cut(new, cut_all=False))
#借助字典对于train_set1进行处理，通过词频向量化
#corpora = tfidf[corpus]

#tfidf = models.TfidfModel(corpus)
tfidf = models.TfidfModel.load('主题词转换txt/qiche/70/tfidf_qiche.tfidf_model')

print(corpus)
print(type(corpus))
print(tfidf[corpus])

#tfidf = models.TfidfModel(corpus)  #转化为tfidf 模型
corpus_tfidf = tfidf[corpus]   #通过模型对语料库实施转换,上一步的转化模型生成后，理论上可以对任何向量转化，我们转化我们的语料库

#doc_bow = [(0, 1), (1, 1)]
# print(tfidf[doc_bow]) # 第二步 -- 使用模型转换向量

#corpus = [dic.doc2bow(text) for text in train_set1]

lda = models.LdaModel.load('主题词转换txt/qiche/70/mylda_qiche.pkl') #LDA模型

corpus_lda = lda[corpus_tfidf]     #将corpus_tfidf再次转化为lda模型的格式，输出的结果中貌似没用到
print(type(corpus_lda))
# num_topics是要训练出来的主题数量,是潜在维度，print_topic是打印主题。结果中整个的一行，0.008*啥+。。。。。这一行是一个主题。for i in range(0, 13)这就相当于13个主题，并且不一定是每个主题都和全部文档关联性很强
#print corpus_lda

print('=======================================================')
for j in range(0, 50):
    print(lda.print_topic(j,topn=20))

print '方法1'
for text in corpus_lda: # both bow->tfidf and tfidf->lsi transformations are actually executed here, on the fly
    print(text)
#打印出来的是和100个主题的其中某些的相似度,因为提取模型时确定了num_topics为100
#print(corpora)
print '方法2'
#print corpus_lda   这个是没问题的

arr = []
for i in lda.get_document_topics(corpus):
    print i
    arr.append(i)


arr = np.array(arr)
print(arr.shape)
print(arr)
arr = np.delete(arr,0,axis=1)    #从0开始删，或者[1,9]删除1到9个，删除列就是1维度，删除行是0维度
print '='*30
print(arr.shape)
print(arr)
arr.shape = 1,-1
print '='*30
print(arr.shape)
print(arr)
arr1 = flatten(arr) #变成列表了
print arr1[0][1]
print '这是arr1[0]'
print '==================================================='
arr = np.array(arr1[0])
print(arr.shape)
print(arr)


arr2 = np.vstack((arr,arr))
arr2=arr2+arr2
arr3 = np.vstack((arr2,arr))
print(arr3.shape)
print(arr3)

#np.save("tem/河北/hebei.npy",arr2)

#利用这种方法，保存文件的后缀名字一定会被置为.npy，这种格式最好只用
#arr3=np.load("tem/河北/hebei.npy")
print(arr3.shape)
print(arr3)

# http://www.cnblogs.com/itdyb/p/5735911.html   一维数组合并为矩阵
#  http://blog.csdn.net/lql0716/article/details/52595590   二维数组转化一维数组

'''
print type(str(arr[1][0]))
print int(arr[1][0])
if arr[1][0] == 2:
    print '没问题'

'''
arr = np.array([])
a = np.array([])
print a.shape
if arr.shape == (0,):
    print '没问题'