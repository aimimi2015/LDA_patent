# encoding=utf-8
import csv
import sys
import jieba, os
from gensim import corpora, models, similarities
import logging
import jieba.posseg
import time

print('程序开始')
print(time.strftime('%Y-%m-%d %H:%M:%S',time.localtime(time.time())))

jieba.load_userdict("词典/自定义词典1.txt")
#jieba.load_userdict("dic/baidu.txt")
jieba.load_userdict("词典/自定义词典2.txt")
jieba.load_userdict("词典/材料科学与工程.txt")
jieba.load_userdict("词典/机械工程词汇大全.txt")
jieba.load_userdict("词典/汽车行业专业词汇.txt")
jieba.load_userdict("词典/汽车专业词库.txt")



print('读取自定义词库完成')
print(time.strftime('%Y-%m-%d %H:%M:%S',time.localtime(time.time())))


#reader = csv.reader(csvfile)

#for line in reader:
#    str = line[17]

train_set1 = []

guosheng = {}.fromkeys([line.rstrip() for line in open('guosheng2.txt')])
stopwords = {}.fromkeys([line.rstrip() for line in open('停用词.txt')])   #fromkeys该方法用于重建一个字典
cipinstop = {}.fromkeys([line.rstrip() for line in open('cipinstop.txt')])

print('读取停用词，停用词频完成')
print(time.strftime('%Y-%m-%d %H:%M:%S',time.localtime(time.time())))
print('='*30)

rode =[]
num=0


walk = os.walk('../pat')
for root, dirs, files in walk:
    for name in files:
        str1 = os.path.join(root, name)
        str3 = 'DS_Store'
        numDS = str1.count(str3)
        if numDS == 0:
            rode.append(os.path.join(root, name))

#print len(rode)

l=0
while num<len(rode):
    filename = rode[num]
    print filename
    print num
    csvfile = open(filename, 'rb')
    reader = csv.reader(csvfile)
    str10 = '汽车'
    for line in reader:

        if line[3]=='':
            continue
        str3 = line[10]
        str1 = str3[0:4]
        str2 = int(str1)
        list1 = list(line[1])
        if line[1]=='':
            continue
        if str2 < 2005:
            continue
        if line[16] == '':
            #print '到17'
            continue
        if line[15] == '':
            #print '到15'
            continue
        str15 = line[15]
        if list1[6]!= '1' and list1[6]!= '2':
            continue
        if str10 not in line[2]:
            continue
        if str15 in guosheng:
            segs = list(jieba.cut(line[16], cut_all=False))
            final = []
            for seg in segs:
                seg = seg.encode('utf-8')
                seg = seg.strip()  # seg的格式是字符串，该函数可以去除字符串的空格
                words = jieba.posseg.cut(seg)  # 进行词性标注部分

                for w in words:
                    #if len(list(seg.decode("utf-8"))) == 1:  # 如果是一个单字，就不要
                        #continue
                    if w.flag.encode("utf-8") not in cipinstop:  # w.flag是w的词性    cipinstop是删除词性的
                        break
                    if seg in stopwords:
                        break
                    final.append(seg)
            l=l+1 #共有多少行数据参与lda计算

            train_set1.append(final)
        else:
            continue

    csvfile.close()
    num=num+1

    print('完成一个csv文件')
    print(time.strftime('%Y-%m-%d %H:%M:%S',time.localtime(time.time())))
    print('='*30)
#print rode[2]

print(l)

print('创建语料库完成')
print(time.strftime('%Y-%m-%d %H:%M:%S',time.localtime(time.time())))
print('='*30)

k=10
k1=str(k)

dic = corpora.Dictionary(train_set1)    #对语料库建立字典
#dic.save('tem/qiche/'+k1+'/dict_quanguo.dict')    #存字典在本地
#dic.save('tem/船舶/dict_船舶.dict')    #存字典在本地
#dic.save('tem/电机/dict_电机.dict')    #存字典在本地

print('对语料库建立字典并存储完成')
print(time.strftime('%Y-%m-%d %H:%M:%S',time.localtime(time.time())))
print('='*30)

corpus = [dic.doc2bow(text) for text in train_set1]   #借助字典对于train_set1进行处理，通过词频向量化
#corpora.MmCorpus.serialize('tem/qiche/20/corpus.mm', corpus)     #c存入硬盘以备后需，相似度接口会用到
#corpora.MmCorpus.serialize('tem/船舶/corpus.mm', corpus)
#corpora.MmCorpus.serialize('tem/电机/corpus.mm', corpus)

print('语料处理词频向量化并存储完成')
print(time.strftime('%Y-%m-%d %H:%M:%S',time.localtime(time.time())))
print('='*30)

tfidf = models.TfidfModel(corpus)  #转化为tfidf 模型

#tfidf.save('tem/qiche/'+k1+'/tfidf_quanguo.tfidf_model')
#tfidf.save('tem/tfidf_飞行航空.pkl')
#tfidf.save('tem/船舶/tfidf_船舶.tfidf_model')
#tfidf.save('tem/电机/tfidf_电机.tfidf_model')


print('转化为tfidf 模型并存储完成')
print(time.strftime('%Y-%m-%d %H:%M:%S',time.localtime(time.time())))
print('='*30)

corpus_tfidf = tfidf[corpus]   #通过模型对语料库实施转换,上一步的转化模型生成后，理论上可以对任何向量转化，我们转化我们的语料库

print('通过模型对语料库实施转换并存储完成')
print(time.strftime('%Y-%m-%d %H:%M:%S',time.localtime(time.time())))
print('='*30)

lda = models.LdaModel(corpus_tfidf,id2word = dic,alpha='auto',eta='auto',num_topics =k,iterations=1000)   #LDA模型  alpha='auto', eta='auto',
#lda.save('tem/qiche/'+k1+'/mylda_quanguo.pkl')
#lda.save('tem/船舶/mylda_船舶.pkl')
#lda.save('tem/电机/mylda_电机.pkl')

print('lda模型存储完成')
print(time.strftime('%Y-%m-%d %H:%M:%S',time.localtime(time.time())))
print('='*30)

# num_topics是要训练出来的主题数量,是潜在维度，print_topic是打印主题。结果中整个的一行，0.008*啥+。。。。。这一行是一个主题。for i in range(0, 13)这就相当于13个主题，并且不一定是每个主题都和全部文档关联性很强

k=k-1
for j in range(0, k):
    print(lda.print_topic(j,topn=25))

print('输出主题')
print(time.strftime('%Y-%m-%d %H:%M:%S', time.localtime(time.time())))
#lda = models.LdaModel.load('mylda_v2.pkl')
#dictionary = corpora.Dictionary.load('dict_v2.dict')


