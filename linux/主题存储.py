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
import json


# 创建连接
jieba.load_userdict("词典/自定义词典1.txt")
jieba.load_userdict("词典/自定义词典2.txt")
jieba.load_userdict("词典/专利发明词条.txt")
jieba.load_userdict("词典/材料科学与工程.txt")
jieba.load_userdict("词典/机械工程词汇大全.txt")
jieba.load_userdict("词典/汽车专业词库.txt")
jieba.load_userdict("词典/汽车行业专业词汇.txt")

stopwords = {}.fromkeys([line.rstrip() for line in open('停用词.txt')])   #fromkeys该方法用于重建一个字典

cipinstop = {}.fromkeys([line.rstrip() for line in open('cipinstop.txt')])
guosheng = {}.fromkeys([line.rstrip() for line in open('guosheng2.txt')])


print('读取停用词，停用词频完成')
print(time.strftime('%Y-%m-%d %H:%M:%S',time.localtime(time.time())))
print('='*30)

rode =[]
num=0


walk = os.walk('../patent')
for root, dirs, files in walk:
    for name in files:
        str1 = os.path.join(root, name)
        str3 = 'DS_Store'
        numDS = str1.count(str3)
        if numDS == 0:
            rode.append(os.path.join(root, name))
print (json.dumps(rode, encoding='UTF-8', ensure_ascii=False)+"\n")

pi = 0
while num<len(rode):
    filename = rode[num]

    csvfile = open(filename, 'rb')
    reader = csv.reader(csvfile)
    print filename
    str10 = '汽车'
    for line in reader:
        arr = []
        if line[3]=='':
            continue
        str3 = line[10]
        str1 = str3[0:4]
        str2 = int(str1)
        list1 = list(line[1])
        if line[1]=='':
            continue
            #<2005
        if str2 < 2005:
            continue
        if line[16] == '':
            continue
        if list1[6] != '1' and list1[6] != '2':
            continue
        if str10 not in line[2]:
            continue
        if line[15] == '':
            continue
        if line[15] in guosheng:
            segs = list(jieba.cut(line[16], cut_all=False))
            final = []
            pd = line[10]
            listpd = pd.split('-')
            pd = (listpd[0], listpd[1])
            pd = "".join(pd)
            pd = int(pd)

            connect = pymysql.connect(host='localhost',
                                      port=3306, user='root',
                                      passwd='123456',
                                      db='test2',
                                      charset='utf8')

            cursor = connect.cursor()

            for seg in segs:
                seg = seg.encode('utf-8')
                seg = seg.strip()  # seg的格式是字符串，该函数可以去除字符串的空格,详见25-36行
                words = jieba.posseg.cut(seg)
                for w in words:
                    if w.flag.encode("utf-8") not in cipinstop:  # w.flag是w的词性    cipinstop是删除词性的
                        break
                    if seg in stopwords:
                        break
                    final.append(seg)

            new = "".join(final)

            dic = corpora.Dictionary.load('../主题词转换txt/qiche/70/dict_qiche.dict')
            corpus = dic.doc2bow(jieba.cut(new, cut_all=False))

            lda = models.LdaModel.load('../主题词转换txt/qiche/70/mylda_qiche.pkl')  # LDA模型

            #===================#===================#===================#===================

            for i in lda.get_document_topics(corpus):
                arr.append(i)
            arr = np.array(arr)
            arr = np.delete(arr, 0, axis=1)  # 从0开始删，或者[1,9]删除1到9个，删除列就是1维度，删除行是0维度
            arr.shape = 1, -1

            arr = flatten(arr)  # 变成列表了
            tarr = arr[0]
            #pi1=str(pi)


            #如果改主题数，那么这些语句都要改
            sl1 = 'topic1, topic2, topic3, topic4, topic5, topic6, topic7, topic8, topic9, topic10, topic11, topic12, topic13, topic14, topic15, topic16, topic17, topic18, topic19, topic20, topic21, topic22, topic23, topic24, topic25, topic26, topic27, topic28, topic29, topic30,topic31, topic32, topic33, topic34, topic35, topic36, topic37, topic38, topic39, topic40,topic41, topic42, topic43, topic44, topic45, topic46, topic47, topic48, topic49, topic50,topic51, topic52, topic53, topic54, topic55, topic56, topic57, topic58, topic59, topic60,topic61, topic62, topic63, topic64, topic65, topic66, topic67, topic68, topic69, topic70'
            sl2 = 'topic101, topic102, topic103, topic104, topic105, topic106, topic107, topic108, topic109, topic110, topic111, topic112, topic113, topic114, topic115, topic116, topic117, topic118, topic119, topic120, topic121, topic122, topic123, topic124, topic125, topic126, topic127, topic128, topic129, topic130,topic131, topic132, topic133, topic134, topic135, topic136, topic137, topic138, topic139, topic140,topic141, topic142, topic143, topic144, topic145, topic146, topic147, topic148, topic149, topic150,topic151, topic152, topic153, topic154, topic155, topic156, topic157, topic158, topic159, topic160,topic161, topic162, topic163, topic164, topic165, topic166, topic167, topic168, topic169, topic170,topic171, topic172, topic173, topic174, topic175, topic176, topic177, topic178, topic179, topic180, topic181, topic182, topic183, topic184, topic185, topic186, topic187, topic188, topic189, topic190, topic191, topic192, topic193, topic194, topic195, topic196, topic197, topic198, topic199, topic200, '
            sl3 = 'topic201, topic202, topic203, topic204, topic205, topic206, topic207, topic208, topic209, topic210, topic211, topic212, topic213, topic214, topic215, topic216, topic217, topic218, topic219, topic220, topic221, topic222, topic223, topic224, topic225, topic226, topic227, topic228, topic229, topic230'

            sql = "insert into qiche (pid,ic1,pd," + sl1+ ") VALUES ('" +line[1]+"','"+line[5] + "',%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s," \
                                                                                        "%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s," \
                                                                                        "%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s," \
                                                                                        "%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)" %(pd,tarr[0],tarr[1],tarr[2],tarr[3],tarr[4],tarr[5],tarr[6],tarr[7],tarr[8],tarr[9],tarr[10],tarr[11],tarr[12],tarr[13],tarr[14],tarr[15],tarr[16],tarr[17],tarr[18],tarr[19],tarr[20],tarr[21],tarr[22],tarr[23],tarr[24],tarr[25],tarr[26],tarr[27],tarr[28],tarr[29],tarr[30],tarr[31],tarr[32],tarr[33],tarr[34],tarr[35],tarr[36],tarr[37],tarr[38],tarr[39],tarr[40],tarr[41],tarr[42],tarr[43],tarr[44],tarr[45],tarr[46],tarr[47],tarr[48],tarr[49],tarr[50],tarr[51],tarr[52],tarr[53],tarr[54],tarr[55],tarr[56],tarr[57],tarr[58],tarr[59],tarr[60],tarr[61],tarr[62],tarr[63],tarr[64],tarr[65],tarr[66],tarr[67],tarr[68],tarr[69])

            #
            #,tarr[80],tarr[81],tarr[82],tarr[83],tarr[84],tarr[85],tarr[86],tarr[87],tarr[88],tarr[89],tarr[90],tarr[91],tarr[92],tarr[93],tarr[94],tarr[95],tarr[96],tarr[97],tarr[98],tarr[99],tarr[100],tarr[101],tarr[102],tarr[103],tarr[104],tarr[105],tarr[106],tarr[107],tarr[108],tarr[109],tarr[110],tarr[111],tarr[112],tarr[113],tarr[114],tarr[115],tarr[116],tarr[117],tarr[118],tarr[119],tarr[120],tarr[121],tarr[122],tarr[123],tarr[124],tarr[125],tarr[126],tarr[127],tarr[128],tarr[129],tarr[130],tarr[131],tarr[132],tarr[133],tarr[134],tarr[135],tarr[136],tarr[137],tarr[138],tarr[139],tarr[140],tarr[141],tarr[142],tarr[143],tarr[144],tarr[145],tarr[146],tarr[147],tarr[148],tarr[149],tarr[150],tarr[151],tarr[152],tarr[153],tarr[154],tarr[155],tarr[156],tarr[157],tarr[158],tarr[159],tarr[160],tarr[161],tarr[162],tarr[163],tarr[164],tarr[165],tarr[166],tarr[167],tarr[168],tarr[169],tarr[170],tarr[171],tarr[172],tarr[173],tarr[174],tarr[175],tarr[176],tarr[177],tarr[178],tarr[179],tarr[180],tarr[181],tarr[182],tarr[183],tarr[184],tarr[185],tarr[186],tarr[187],tarr[188],tarr[189],tarr[190],tarr[191],tarr[192],tarr[193],tarr[194],tarr[195],tarr[196],tarr[197],tarr[198],tarr[199],tarr[200],tarr[201],tarr[202],tarr[203],tarr[204],tarr[205],tarr[206],tarr[207],tarr[208],tarr[209],tarr[210],tarr[211],tarr[212],tarr[213],tarr[214],tarr[215],tarr[216],tarr[217],tarr[218],tarr[219],tarr[220],tarr[221],tarr[222],tarr[223],tarr[224],tarr[225],tarr[226],tarr[227],tarr[228],tarr[229]
            # VALUES ('" + line[5] + "',%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)" %(pd,tarr[0],tarr[1],tarr[2],tarr[3],tarr[4],tarr[5],tarr[6],tarr[7],tarr[8],tarr[9],tarr[10],tarr[11],tarr[12],tarr[13],tarr[14])

            #print sql

            '''
            cursor.execute(sql)
            connect.commit()
            cursor.close()
            connect.close()
            '''
            # print(sql)  '" + pi1 + "','" + line[5] + "',%s,

            try:
                cursor.execute(sql)
                connect.commit()
            except Exception:
                print 'chucuole'
                #print Exception
                connect.rollback()
            finally:
                cursor.close()
                connect.close()


            # ===================#===================#===================#===================
        else:
            continue


    csvfile.close()
    num=num+1
    print('完成一个csv文件')
    print(time.strftime('%Y-%m-%d %H:%M:%S',time.localtime(time.time())))
    print('='*30)
