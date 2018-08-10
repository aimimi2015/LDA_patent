# coding: utf-8
#使用非线性最小二乘法拟合
import matplotlib.pyplot as plt
from scipy.optimize import curve_fit
import numpy as np
import sys
reload(sys)
sys.setdefaultencoding('utf8')
from matplotlib.font_manager import FontProperties
font = FontProperties(fname='/Library/Fonts/st.otf')

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




#topic30 示例主题
x2=[0.007838745800671893, 0.01866368047779022, 0.04180664427025009, 0.06681597611048899, 0.0925718551698395, 0.1362448674878686, 0.1952220977976857, 0.2866741321388578, 0.4087346024636058, 0.5651362448674878, 0.7741694662187384, 1.0]
#12年 IVI

x3=[0.014297729184188394, 0.03868797308662742, 0.0798990748528175, 0.127838519764508, 0.16568544995794784, 0.23549201009251472, 0.3187552565180824, 0.4272497897392767, 0.5542472666105971, 0.6938603868797308, 0.8427249789739276, 1.0]
#12年 RTI


x5=[0.151,0.314,0.4535,0.64,0.744,0.791,0.84,0.91,1]
#探测点 0.07,0.13,0.27,0.39,0.55,0.64,0.68,0.72,0.78,0.86，0.92,0.97,1.0]


#plot_new2 = plt.plot(x2,'*',color='green')
#plot_new1 = plt.plot(x1,y1,'r',label='RTI',linewidth=1.5,color='red')

#plot_new1 = plt.plot(x1,'*',color='black')
plot_new2 = plt.plot(x2,'*',color='green')
plot_new3 = plt.plot(x3,'*',color='yellow')
#plot_new = plt.plot(x5,'*',color='red')

x4=np.linspace(0, 8, 9)
#plot_new4 = plt.plot(x4,x1,'r',label='IVI-2013',linewidth=1.5,color='black')
plot_new5 = plt.plot(x,x2,'r',label='IVI',linewidth=1.5,color='red',linestyle='--')
plot_new6 = plt.plot(x,x3,'r',label='TRI',linewidth=1.5,color='blue',linestyle=':')
#plot_new7 = plt.plot(x4,x5,'r',label='RTI-2013',linewidth=1.5,color='red')


plot1=plt.plot(x, y, label='NI',linewidth=1.5,color='green')
str=u"这里就可以用中文了"
plt.xlabel('相对年份',fontproperties=font,fontsize=15)
plt.ylabel('指标值',fontproperties=font,fontsize=15)
plt.legend(loc=4)#指定le.
# gend的位置,读者可以自己help它的用法
#plt.title('主题探测点',fontproperties=font)

plt.show()
plt.savefig('p2.png')
