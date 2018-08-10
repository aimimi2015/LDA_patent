# coding: utf-8
#使用非线性最小二乘法拟合
import matplotlib.pyplot as plt
from scipy.optimize import curve_fit
import numpy as np
#用指数形式来拟合
x = np.linspace(0, 11, 12)

def func(x):
    return np.math.pow(0.85, x)

y = []
i=0
while i<12:

    y.append(func(x[i]))
    i=i+1
print len(x)
print len(y)

# yvals= np.math.pow(x, 0.85)
#下降
#x2 = [0.008,0.024,0.04,0.08,0.144,0.232,0.304,0.44,0.592,0.8,0.88,0.944,1.0]
#上升12年
x2 = [0.0152,0.0238,0.0476,0.0857,0.1581,0.19,0.232,0.3524,0.496,0.60,0.769,1.0]

x1 = np.linspace(0, 11, 12)
# y1 = [0,0.03,0.12,0.21,0.24,0.26,0.30,0.38,0.42,0.54,0.65,0.86,1.0]
y1 = [0.0152,0.0238,0.0476,0.0857,0.1581,0.19,0.232,0.3524,0.496,0.60,0.769,1.0]

# plot_new1 = plt.plot(x1,  'r', label='original values',linewidth=1.5,color='red')
# plt.xlabel('year(05-15)')
# plt.ylabel('Proportion')
# plt.legend(loc=4)  # 指定legend的位置
# plt.title('topic20')
# plt.show()
# plt.savefig('p1.png')

plot_new2 = plt.plot(x2,'*',color='green')
plot_new1 = plt.plot(x1,y1,'r',label='IVII',linewidth=1.5,color='red')
plot1=plt.plot(x, y, label='NI',linewidth=1.5,color='blue')
plt.xlabel('j')
plt.ylabel('Issued volume index,IVI')
plt.legend(loc=4)#指定le.
# gend的位置,读者可以自己help它的用法
plt.title('Detection point of topic')
plt.show()
plt.savefig('p2.png')
