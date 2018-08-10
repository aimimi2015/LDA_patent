# coding: utf-8

import matplotlib.pyplot as plt

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

y1=[1,0.5,0.33,0.25,0.2,0.167,0.143,0.125,0.111,0.1,0.091,0.083]

x2=y
plot_new2 = plt.plot(x2,'*')
plot_new3 = plt.plot(y1,'*')

plot1=plt.plot(x, y, label='NI',linewidth=1.5,linestyle='--')
plot2=plt.plot(x, y1, 'r',label='NI-original',linewidth=1.5,color='green')


plt.xlabel('相对年份',fontproperties=font,fontsize=15)
plt.ylabel('新颖度指标值',fontproperties=font,fontsize=15)
plt.legend(loc=4)#指定le.
# gend的位置,读者可以自己help它的用法
#plt.title('Novelty index',fontproperties=font)
plt.plot(x,y1)
plt.show()
plt.savefig('p2.png')
