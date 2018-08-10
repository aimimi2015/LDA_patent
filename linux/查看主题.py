# encoding=utf-8
import csv
import sys
import jieba, os
from gensim import corpora, models, similarities
import logging
import jieba.posseg
import time


#LDA模型  alpha='auto', eta='auto',
lda=models.LdaModel.load('tem/230-2/mylda_quanguo.pkl')
#lda.save('tem/船舶/mylda_船舶.pkl')
#lda.save('tem/电机/mylda_电机.pkl')



# num_topics是要训练出来的主题数量,是潜在维度，print_topic是打印主题。结果中整个的一行，0.008*啥+。。。。。这一行是一个主题。for i in range(0, 13)这就相当于13个主题，并且不一定是每个主题都和全部文档关联性很强
for j in range(0, 230):
    print(lda.print_topic(j,topn=10))

print('输出主题')
print(time.strftime('%Y-%m-%d %H:%M:%S', time.localtime(time.time())))
#lda = models.LdaModel.load('mylda_v2.pkl')
#dictionary = corpora.Dictionary.load('dict_v2.dict')


