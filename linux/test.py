# -*- coding:utf-8 -*-
# **********************************
# ** http://weibo.com/lixiaodaoaaa #
# ** create at 2017/5/20   20:55 ***
# ****** by:lixiaodaoaaa ***********


import numpy as np
import pandas as pd
import matplotlib
import pylab
from matplotlib.font_manager import FontManager, FontProperties
import subprocess
import matplotlib.pyplot as plot


def getChineseFont():
    return FontProperties(fname='/Library/Fonts/t.ttc')

if __name__ == '__main__':
    plot.title(u"我是道哥", fontproperties=getChineseFont())
    plot.show()