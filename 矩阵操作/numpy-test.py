#coding=utf-8
import numpy as np
import sys
import os

def func2(i, j):
    return (i + 1) * (j + 1)

print(np.fromfunction(func2, (8,6)))

a = np.arange(10)
print(a[3:])

print(a[5:1:-2])

x = np.arange(10,1,-1)
print x[[3, 3, 1, 8]]
b = x[np.array([3,3,-3,8])]
print np.array([3,3,-3,8])
print b
b[2] = 100
print b

x = np.arange(5,0,-1)
print np.array([True, False, True, False, False])
print x[np.array([True, False, True, False, False])]

print np.arange(0, 60, 10)
print np.arange(0, 60, 10).reshape(-1, 1) + np.arange(0, 6)

import time
import math

x = [i * 0.001 for i in xrange(1000000)]
start = time.clock()
for i, t in enumerate(x):
    x[i] = math.sin(t)
print "math.sin:", time.clock() - start

x = [i * 0.001 for i in xrange(1000000)]
x = np.array(x)
start = time.clock()
np.sin(x,x)
print "numpy.sin:", time.clock() - start



mylist = ["It's", 'only', 'a', 'model']

for i in mylist:
    print(i)

print np.arange(12).reshape(2, 3, 2)


a = np.arange(8)
b = np.add.accumulate(a)
c = a + b
f = open("tem/result.npy", "wb")
np.save(f, a) # 顺序将a,b,c保存进文件对象f
np.save(f, b)
np.save(f, c)
f.close()
f = open("tem/result.npy", "rb")
print np.load(f) # 顺序从文件对象f中读取内容
print np.load(f)
print np.load(f)


np.save("tem/a.npy", a)
c = np.load( "tem/a.npy" )
print c



a = np.array([[1,2,3],[4,5,6]])
b = np.arange(0, 1.0, 0.1)
c = np.sin(b)
np.savez("tem/result.npz", a, b, sin_array = c)
r = np.load("tem/result.npz")
print r["arr_0"] # 数组a

print r["arr_1"] # 数组b
print r["sin_array"] # 数组c

