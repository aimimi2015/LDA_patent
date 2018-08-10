# -*- coding: utf-8 -*-
import numpy as np
import matplotlib.pyplot as plt


plt.subplot(431) # 画的是共有四行三列，然后这是4*3这12个位置中的第三个
plt.subplot(432) # 画的是共有四行三列，然后这是4*3这12个位置中的第2个
plt.subplot(427) # 画的是共有四行2列，然后这是4*3这12个位置中的第7个
plt.show()



fig = plt.figure()
ax = fig.add_axes([0.35, 0.4, 0.3, 0.7])
line, = ax.plot([1,2,3],[1,2,1])
plt.show()