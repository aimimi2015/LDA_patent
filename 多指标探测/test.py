# coding: utf-8
from __future__ import print_function
from __future__ import print_function
from __future__ import print_function
import matplotlib.pyplot as plt
import numpy as np
import pickle
import pprint
import matplotlib.pyplot as plt
import numpy as np
import pymysql
import pickle
import json
from sympy import *



# tem='asdhakd/asd'
# num = tem.index('/')
# tem=tem[0:num]
#
# print tem
# tem=1
# tem2=100
# tem2=float(tem2)
# print tem / tem2
# topici_year=[1,1,3,6,1,8,4,1,22,11,1,10]
#
#
# x = 2007- 2005
# totol = topici_year[0]
# while (x > 0):  # 求totol
#     totol = totol + topici_year[x]  # 第一个加最后一个
#     x = x - 1
# print totol
# #
# j = 2005
# while (j < 2017):
#     list = []
#     m = j - 2004  # 求一共有几个IVI
#     n = m
#     p = 1
#     tem = topici_year[0]
#     list.append(tem / 100)
#     while (n > 1):
#         tem = tem + topici_year[p]
#         list.append(tem / 100)
#         print tem / 100
#
#         p = p + 1
#         n = n - 1
#     j=j+1

#
#
# rode =[]
# num=0
#
#
# walk = os.walk('../patent')
# for root, dirs, files in walk:
#     for name in files:
#         str1 = os.path.join(root, name)
#         str3 = 'DS_Store'
#         numDS = str1.count(str3)
#         if numDS == 0:
#             rode.append(os.path.join(root, name))
# print (json.dumps(rode, encoding='UTF-8', ensure_ascii=False)+"\n")
#
# x=0
# pi = 0
# while num<len(rode):
#     filename = rode[num]
#
#     csvfile = open(filename, 'rb')
#     reader = csv.reader(csvfile)
#     print filename
#     str10 = '汽车'
#     for line in reader:
#         arr = []
#         if line[3]=='':
#             continue
#         str3 = line[10]
#         str1 = str3[0:4]
#         str2 = int(str1)
#         list1 = list(line[1])
#         if line[1]=='':
#             continue
#             #<2005
#         if str2 < 2005:
#             continue
#         if line[16] == '':
#             continue
#         if list1[6] != '1' and list1[6] != '2':
#             continue
#         if str10 not in line[2]:
#             continue
#         x=x+1
#
#     csvfile.close()
#     num=num+1
#     print('完成一个csv文件')
#     print(time.strftime('%Y-%m-%d %H:%M:%S',time.localtime(time.time())))
#     print('='*30)
#
# print x


#
# xinxing=[3,4,5,6]
# n=3
# print xinxing.count(n)
#
# x1 = np.arange(1, 30, 1)
# # y = np.array([4.00, 6.40, 8.00, 8.80, 9.22, 9.50, 9.70, 9.86, 10.00, 10.20, 10.32, 11.42, 12.00, 12.42, 13.00, 15.00, 16.20, 17.32, 19.42, 21.00])
#
# m=4.5
# m=int(m)
#
# y1=[]
#
# # 获取游标
# n=0
# while(n<71):
#
#     if(xinxing.count(n)>0):
#         print 'asd®'
#     n = n + 1


pkl_file = open('zhichidoc.pkl', 'rb')
zhichidoczongshu = pickle.load(pkl_file)
pkl_file.close()
print(json.dumps(zhichidoczongshu, encoding='UTF-8', ensure_ascii=False))

j=0

while j<70:
    if (j%10==0):
        print ('-====')
    print(zhichidoczongshu[j])
    j=j+1

j=0
sum=0
while(j<70):
    sum=sum+zhichidoczongshu[j]
    j=j+1
print(sum)

j=0
while(j<70):
    x = -1
    max = 0
    i = 0
    while(i<70):


        if zhichidoczongshu[i]>max:
            max=zhichidoczongshu[i]
            x=i+1
        i = i + 1
    zhichidoczongshu[x-1] = 0

    print(max)
    print(x),print('topic')


    j=j+1



output = open('RTIdoc/RTIdoc_topic30.pkl', 'rb')
list1=pickle.load(output)
print(json.dumps(list1, encoding='UTF-8', ensure_ascii=False))

output.close()