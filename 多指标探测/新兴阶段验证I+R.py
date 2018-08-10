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

flag=0
zhengque1=0
cuowu1=0
zhengque2=0
cuowu2=0

n=1
while (n < 71):
    pkl_file = open('突破时间/I+Rtopic.pkl', 'rb')
    tupo = pickle.load(pkl_file)
    #print(json.dumps(tupo, encoding='UTF-8', ensure_ascii=False))

    pkl_file.close()
    pkl_file = open('结束时间/I+Rtopic.pkl', 'rb')
    tupo2 = pickle.load(pkl_file)
    #print(json.dumps(tupo2, encoding='UTF-8', ensure_ascii=False))
    pkl_file.close()

    y1 = []
    if (tupo[n-1] != -1 ):
        if(tupo2[n-1] == -1):
            m2=9.5
        else:
            m2 = tupo2[n - 1]
        m = tupo[n - 1]
        #m2 = tupo2[n - 1]
        x = m2 - m
        x2 = x+1
        # print(x2)
        x3=x2
        if(m==-0.5):
            m=-1
        else:
            m = int(m)
        # print (m)


        year1=m+2007
        i=1


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
                #print(json.dumps(listzhichi, encoding='UTF-8', ensure_ascii=False))
                pkl_file.close()
                    #主题是n，月份是m年前后的36月
                j=0
                zong=0
                while(j<70):
                    zong=zong+listzhichi[j]
                    j=j+1
                zong=float(zong)
                zong=zong/10000
                #print (zong)
                y1.append(listzhichi[n-1])
                i = i + 1
            year1=year1+1
            x2=x2-1
            #print('一年')

        w = 12*x3 + 1-12

        x1 = np.arange(1, w, 1)

        y1=y1[6:len(y1)-6]


        #print (len(x1))
        #print (len(y1))

        #print(json.dumps(y1, encoding='UTF-8', ensure_ascii=False))

        y1 = np.array(y1)
        #求支持文档的强度把

        #print(json.dumps(list1 , encoding='UTF-8', ensure_ascii=False))

        #print len(list1)


        z1 = np.polyfit(x1, y1, 2)  # 用3次多项式拟合
        p1 = np.poly1d(z1)

        yvals = p1(x1)
        p2 = abs(yvals - y1)
        sigma = np.std(p2)
        #print(sigma)
        #print(p2)

        # print ("p1:"),
        # print(p1)
        # print("p1:"),


    # if((p1[2]>0 and p1[1]/p1[2]<0)or(p1[2]<0 and -p1[1]/2*p1[2])>6*x3):
    #     zhengque=zhengque+1
    # else:
    #     cuowu=cuowu+1
    #

        a = float(p1[2])
        b = float(p1[1])
        # print(a)
        # print(b)
        c = b / (2 * a)
        c = -1 * c

        # print(c)

        n2 = 6 * x3+0.5
        # print(n2)
        # print('topic' + str(n)),
        if (a > 0 and c < n2):
            # print('类型一')
            zhengque1 = zhengque1 + 1
        elif (a > 0 and c >= n2):
            # print('类型二')
            cuowu1 = cuowu1 + 1
        elif (a < 0 and c <= n2):
            # print('类型三')
            cuowu1 = cuowu1 + 1
        elif (a < 0 and c > n2):
            # print('类型四')
            zhengque1 = zhengque1 + 1



        # print(type(p1))
        yvals = p1(x1)  # 也可以使用yvals=np.polyval(z1,x)
        #ybar = np.sum(y1) / len(y1)

        # print(type(np.mean(p2)))
        #out = p2 > sigma * 3
        # print(type(out))
        # print (out)

        #ssreg = np.sum((yvals - ybar) ** 2)  # 拟合数据方差
        #sstot = np.sum((y1 - ybar) ** 2)  # 原始数据方差
        # print (ssreg / sstot)  # 准确率

        plot1 = plt.plot(x1, y1, '*', label='original values')
        plot2 = plt.plot(x1, yvals, 'r', label='polyfit values')
        plt.xlabel('year(05-15)')
        plt.ylabel('Proportion')
        plt.legend(loc=4)  # 指定legend的位置,读者可以自己help它的用法
        plt.title('topic1')
        plt.plot(x1, y1)
        ##plt.show()
        plt.savefig('p1.png')

        y_new = y1.tolist()  # 准备修改    这就是之后被替换的新的y分布
        yvals1 = yvals.tolist()  # 准备修改

        #
        # def quzao(sigma,y_new,yvals1):
        #     i=0
        #     while i < len(y_new):
        #         if abs(y_new[i] - yvals1[i]) >= sigma * 3:
        #             print(y_new[i])
        #             if i != 0 and i != len(y) - 1:
        #                 y_new[i] = (y_new[i - 1] + y_new[i - 2]) * 0.5
        #
        #             elif i == len(y) - 1:
        #                 y_new[i] = (y_new[len(y) - 2] + y_new[len(y) - 3]) * 0.5
        #
        #             z1 = np.polyfit(x, y_new, 2)  # 用3次多项式拟合
        #             p1 = np.poly1d(z1)
        #
        #         i = i + 1


        while True:
            i = 0
            while i < len(y1):
                if abs(y_new[i] - yvals1[i]) >= sigma * 3:
                    # print(y_new[i])
                    if i != 0 and i != len(y1) - 1:
                        y_new[i] = (y_new[i - 1] + y_new[i +1]) * 0.5
                    elif i == 1:
                        y_new[i] = (y_new[0] + y_new[2]) * 0.5

                        # z1 = np.polyfit(x, y_new, 2)  # 用3次多项式拟合
                        # p1 = np.poly1d(z1)


                        # yvals_new = p1(x1)
                        # plot_new1 = plt.plot(x1, y_new, '*', label='original values')
                        # plot_new12 = plt.plot(x1, yvals_new, 'r', label='polyfit values')
                        # plt.xlabel('x axis')
                        # plt.ylabel('y axis')
                        # plt.legend(loc=4)  # 指定legend的位置
                        # plt.title('polyfitting')
                        # plt.show()
                        # print('========')

                i = i + 1
            z1 = np.polyfit(x1, y_new, 2)  # 用3次多项式拟合
            p1 = np.poly1d(z1)

            yvals = p1(x1)
            p2 = abs(yvals - y_new)
            sigma1 = np.std(p2)
            # print(sigma1)
            if (sigma == sigma1):
                break
            else:
                sigma = sigma1

        # print(y_new)

        z_new = np.polyfit(x1, y_new, 2)  # 用3次多项式拟合
        p_new = np.poly1d(z_new)
        yvals_new = p_new(x1)
        #ybar_new = np.sum(y_new) / len(y1)
        #ssreg = np.sum((yvals_new - ybar_new) ** 2)
        #sstot = np.sum((y_new - ybar_new) ** 2)
        #sstot_old = np.sum((y1 - ybar) ** 2)  # 原始数据方差

        #print(ssreg / sstot_old)  # 准确率

        a = float(p_new[2])
        b = float(p_new[1])
        # print(a)
        # print(b)
        c = b / (2 * a)
        c = -1 * c

        # print(c)

        n2 = 6 * x3+0.5
        # print(n2)
        print('topic' + str(n)),
        if (a > 0 and c < n2):
            print('类型一')
            zhengque2 = zhengque2 + 1
        elif (a > 0 and c >= n2):
            print('类型二')
            if (len(x1) == 12):
                flag = flag + 1
            cuowu2 = cuowu2 + 1
        elif (a < 0 and c <= n2):
            print('类型三')
            if (len(x1) == 12):
                flag = flag + 1
            cuowu2 = cuowu2 + 1
        elif (a < 0 and c > n2):
            print('类型四')
            zhengque2 = zhengque2 + 1

        plot_new1 = plt.plot(x1, y_new, '*', label='original values')
        plot_new12 = plt.plot(x1, yvals_new, 'r', label='polyfit values')
        plt.xlabel('month')
        plt.ylabel('doc')
        plt.legend(loc=4)  # 指定legend的位置
        plt.title('topic20')
        plt.plot(x1,y1)
        # plt.show()
        plt.savefig('p1.png')

        # print(p_new)

    n = n + 1

print(zhengque1)
print(cuowu1)
print(zhengque2)
print(cuowu2)
print (flag)