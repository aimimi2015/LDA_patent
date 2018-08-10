# coding: utf-8
#使用非线性最小二乘法拟合
import matplotlib.pyplot as plt
from scipy.optimize import curve_fit
import numpy as np
#用指数形式来拟合
x = np.linspace(0, 9, 10)

def func(x):
    return np.math.pow(0.78, x)

y = []
i=0
while i<10:
    y.append(func(x[i]))
    i=i+1
print len(x)
print len(y)



#9年 IVI
y1=[0.03,0.05,0.10,0.18,0.29,0.38,0.55,0.74,1]
#12年 IVI

y8=[]
i=0
while i<=8:
    y8.append(y1[i]/y1[8])
    i=i+1

y7=[]
i=0
while i<=7:
    y7.append(y1[i]/y1[7])
    i=i+1

y6=[]
i=0
while i<=6:
    y6.append(y1[i]/y1[6])
    i=i+1
y5=[]
i=0
while i<=5:
    y5.append(y1[i]/y1[5])
    i=i+1
y4=[]
i=0
while i<=4:
    y4.append(y1[i]/y1[4])
    i=i+1
y3=[]
i=0
while i<=3:
    y3.append(y1[i]/y1[3])
    i=i+1
y2=[]
i=0
while i<=2:
    y2.append(y1[i]/y1[2])
    i=i+1



x2=[0,1,2]
x3=[0,1,2,3]
x4=[0,1,2,3,4]
x5=[0,1,2,3,4,5]
x6=[0,1,2,3,4,5,6]
x7=[0,1,2,3,4,5,6,7]
x8=[0,1,2,3,4,5,6,7,8]


#plot_new2 = plt.plot(x2,'*',color='green')
#plot_new1 = plt.plot(x1,y1,'r',label='RTI',linewidth=1.5,color='red')

# plot_new1 = plt.plot(x1,'*',color='black')
# plot_new2 = plt.plot(x2,'*',color='green')
# plot_new3 = plt.plot(x3,'*',color='yellow')
# plot_new = plt.plot(x5,'*',color='red')
plot_2 = plt.plot(y2,'*',color='green')
plot_3 = plt.plot(y3,'*',color='green')
plot_4 = plt.plot(y4,'*',color='green')
plot_5 = plt.plot(y5,'*',color='green')
plot_6 = plt.plot(y6,'*',color='green')
plot_7 = plt.plot(y7,'*',color='green')
plot_8 = plt.plot(y8,'*',color='green')

plot_new2 = plt.plot(x2,y2,'r',label='IVI-2007',linewidth=1.5,color='red')
plot_new3 = plt.plot(x3,y3,'r',label='IVI-2007',linewidth=1.5,color='black')
plot_new4 = plt.plot(x4,y4,'r',label='IVI-2008',linewidth=1.5,color='yellow')
plot_new5 = plt.plot(x5,y5,'r',label='IVI-2009',linewidth=1.5,color='pink')
plot_new6 = plt.plot(x6,y6,'r',label='IVI-2010',linewidth=1.5,color='orange')
plot_new7 = plt.plot(x7,y7,'r',label='IVI-2011',linewidth=1.5,color='brown')
plot_new8 = plt.plot(x8,y8,'r',label='IVI-2012',linewidth=1.5,color='purple')

#
# x4=np.linspace(0, 9, 10)
# plot_new4 = plt.plot(x4,x1,'r',label='IVI-2013',linewidth=1.5,color='black')
# plot_new5 = plt.plot(x,x2,'r',label='IVI-2016-decrease',linewidth=1.5,color='green')
# plot_new6 = plt.plot(x,x3,'r',label='IVI-2016-increase',linewidth=1.5,color='yellow')
# plot_new7 = plt.plot(x4,x5,'r',label='RTI-2013',linewidth=1.5,color='red')
#
#
plot1=plt.plot(x, y, label='NI',linewidth=1.5,color='blue')
plt.xlabel('j')
plt.ylabel('index')
plt.legend(loc=4)#指定le.
# gend的位置,读者可以自己help它的用法
plt.title('Detection point of topic')
plt.show()
plt.savefig('p2.png')
