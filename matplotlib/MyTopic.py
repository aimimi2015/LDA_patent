# coding: utf-8
__author__ = 'leilu'
#wordcloud生成中文词云

from wordcloud import WordCloud
import codecs
import jieba
#import jieba.analyse as analyse
from scipy.misc import imread
import os
import numpy as np
from os import path
import matplotlib.pyplot as plt
from PIL import Image, ImageDraw, ImageFont
from wordcloud import WordCloud, STOPWORDS, ImageColorGenerator


d = path.dirname(__file__)

# Read the whole text.
text = open(path.join(d, 'alice.txt')).read()

# 绘制词云
def draw_wordcloud():
    #读入一个txt文件
    d = path.dirname(__file__)
    comment_text = open(path.join(d, 'alice.txt')).read()
    #结巴分词，生成字符串，如果不通过分词，无法直接生成正确的中文词云
    cut_text = " ".join(jieba.cut(comment_text))

    freq =[]
    txt_freq = {"无人机": "0.014", "支座": "0.028", "伺服电机": "0.012", "底盘": "0.016", "外翼": "0.016", "支撑": "0.012", "滑块": "0.027", "立柱": "0.023", "滑动": "0.013", "导轨": "0.042"}
    for k in txt_freq:
        v = txt_freq[k]
        v=float(v)
        k = k.decode("utf-8")  #被解码成Unicode对象
        item = (k,v)
        freq.append(item)


    #freq2 =[('词a', 100),('词b', 90),('词c', 80)]
    #print type(freq2[1])
    # txtFreq例子为[('词a', 100),('词b', 90),('词c', 80)]

    #print cut_text
    #d = path.dirname(__file__) # 当前文件文件夹所在目录
    color_mask = imread("tuoyuan2.png") # 读取背景图片
    cloud = WordCloud(font_path=path.join(d,'ziti/t.ttf'),        #font_path=path.join(d,'simsun.ttc'),
        #设置背景色
        background_color='white',
        #词云形状
        mask=color_mask,
        #允许最大词汇
        max_words=100,
        #最大号字体
        max_font_size=120,
        min_font_size=12,
        width=400, height=370,#有画布就不管用了
        )
    alice_coloring = np.array(Image.open(path.join(d, "alice_color.png")))
    image_colors = ImageColorGenerator(alice_coloring)
    word_cloud = cloud.generate(cut_text) # 产生词云wordcloud = WordCloud().fit_words(frequencies)
    #word_cloud = cloud.fit_words(dict(freq))
    word_cloud.to_file("pjl_cloud4.jpg") #保存图片
    #  显示词云图片
    plt.imshow(word_cloud)
    plt.axis('off')
    #plt.figure()
    plt.show()





if __name__ == '__main__':

    draw_wordcloud()