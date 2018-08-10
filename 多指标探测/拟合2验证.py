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


  #需要判断的主题编号，自己手动改
#
# year=2007
# q=1
# while (q<71):
#     i = 1
#     while (i < 13 and year < 2017):
#         month = 0
#         if i < 10:
#             month = '0' + str(i)
#         else:
#             month = str(i)
#         pkl_file = open('zhichidocmonth/zhichidoc_' + str(year) + month + '.pkl', 'rb')
#         listzhichi = pickle.load(pkl_file)
#         print(json.dumps(listzhichi, encoding='UTF-8', ensure_ascii=False))
#         pkl_file.close()



# y = np.array([4.00, 6.40, 8.00, 8.80, 9.22, 9.50, 9.70, 9.86, 10.00, 10.20, 10.32, 11.42, 12.00, 12.42, 13.00, 15.00, 16.20, 17.32, 19.42, 21.00])









n=1
while (n <71):
    pkl_file = open('突破时间/IVItopic.pkl', 'rb')
    tupo = pickle.load(pkl_file)
    print(json.dumps(tupo, encoding='UTF-8', ensure_ascii=False))

    pkl_file.close()
    pkl_file = open('结束时间/IVItopic.pkl', 'rb')
    tupo2 = pickle.load(pkl_file)
    print(json.dumps(tupo2, encoding='UTF-8', ensure_ascii=False))
    pkl_file.close()

    y1 = []
    if (tupo[n-1] != -1 and tupo2[n-1] != -1):
        m = tupo[n - 1]
        m2 = tupo2[n - 1]
        x = m2 - m
        x2 = x+1
        print(x2)
        x3=x2
        if(m==-0.5):
            m=-1
        else:
            m = int(m)
        print (m)


        year1=m+2007
        i=1

        x2=12
        year1=2007
        while(x2>0):
            i = 1
            while(i<13 and year1>2005 and year1<2017):
                month = 0
                if i < 10:
                    month = '0' + str(i)
                else:
                    month = str(i)
                pkl_file = open('zhichidocmonth/zhichidoc_' + str(year1) + month + '.pkl', 'rb')
                listzhichi = pickle.load(pkl_file)
                print(json.dumps(listzhichi, encoding='UTF-8', ensure_ascii=False))
                pkl_file.close()
                    #主题是n，月份是m年前后的36月
                j=0
                zong=0
                while(j<70):
                    zong=zong+listzhichi[j]
                    j=j+1
                zong=float(zong)
                print (zong)
                y1.append(listzhichi[n - 1] / zong)
                i = i + 1
            year1=year1+1
            x2=x2-1
            print('一年')

        w = 12*10 + 1

        x1 = np.arange(1, w, 1)




        print (len(x1))
        print (len(y1))

        print(json.dumps(y1, encoding='UTF-8', ensure_ascii=False))

        y1 = np.array(y1)
        #求支持文档的强度把

        #print(json.dumps(list1 , encoding='UTF-8', ensure_ascii=False))

        #print len(list1)


        z1 = np.polyfit(x1, y1, 2)  # 用3次多项式拟合
        p1 = np.poly1d(z1)

        yvals = p1(x1)
        p2 = abs(yvals - y1)
        sigma = np.std(p2)
        print(sigma)
        print(p2)

        '''
        具体来说，三西格玛规则是建立在数据服从正态分布的基础之上的，其阈值为
        正态分布平均值与三倍标准差之和。在正态分布中标准差为𝜎，均值为𝜇，对于全部
        的数据来说，数值分布在(𝜇 − 𝜎,𝜇 + 𝜎)中的概率为 0.655，布在(𝜇 − 2𝜎,𝜇 + 2𝜎)中的
        概率为 0.954，分布在(𝜇 − 3𝜎,𝜇 + 3𝜎)中的概率大致为 0.997。规则规定任何大于三
        西格玛阈值的值都极有可能是异常值。因此我们以图 4.3 中程序移除异常值，并进行
        临近数据点平均值替换。

        '''
        print ("p1:"),
        print(p1)  # 在屏幕上打印拟合多项式
        yvals = p1(x1)  # 也可以使用yvals=np.polyval(z1,x)
        #ybar = np.sum(y1) / len(y1)

        #print(type(np.mean(p2)))
        #out = p2>sigma*3
        #print(type(out))
        #print (out)

        #ssreg = np.sum((yvals - ybar) ** 2)   #拟合数据方差
        #sstot = np.sum((y1 - ybar) ** 2)   #原始数据方差
        #print (ssreg / sstot)  # 准确率


        if(n==57):
            plot1 = plt.plot(x1, y1, '*', label='original values')
            # plot2 = plt.plot(x1, yvals, 'r', label='polyfit values')
            plt.xlabel('year(2005-2015)')
            plt.ylabel('Proportion')
            plt.legend(loc=4)  # 指定legend的位置,读者可以自己help它的用法

            topic = 'topic' + str(n)
            plt.title(topic)
            plt.plot(x1, y1)
            plt.show()
            plt.savefig('p1.png')




    n = n + 1