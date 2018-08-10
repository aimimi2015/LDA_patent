# coding: utf-8
#使用非线性最小二乘法拟合
import matplotlib.pyplot as plt
from scipy.optimize import curve_fit
import numpy as np
#用指数形式来拟合
x = np.arange(1, 17, 1)
y = np.array([55.86,88.00,13.00, 16.20, 18.32, 22.42, 29.50, 38.70, 1.00, 2.00, 4.00, 5.80, 6.22, 7.50, 9.70, 11.86])
def func(x,a,b):
    return a*np.exp(b/x)
popt, pcov = curve_fit(func, x, y)
a=popt[0]#popt里面是拟合系数，读者可以自己help其用法
b=popt[1]

yvals=func(x,a,b)

# yvals= np.math.pow(x, 0.85)

print np.math.pow(0.85,6)

print a,b
plot1=plt.plot(x, y, '*',label='original values')
plot2=plt.plot(x, yvals, 'r',label='curve_fit values')
plt.xlabel('x axis')
plt.ylabel('y axis')
plt.legend(loc=4)#指定legend的位置,读者可以自己help它的用法
plt.title('curve_fit')
plt.show()
plt.savefig('p2.png')
