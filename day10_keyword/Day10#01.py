#!/usr/bin/python3.7
# -*- coding: utf-8 -*-
import sys
import json
import pandas as pd
import numpy as np
import codecs
import re
import itertools
import jieba
import wordcloud
import matplotlib
from wordcloud import WordCloud
import matplotlib.pyplot as plt

jieba.load_userdict("dict.txt.big")  # 先載入解析字型
txt_file_path = "data.txt"

# ===============載入檔案到變數中 start==========================
with open(txt_file_path, "r", encoding='utf-8')as fn:
    lines = fn.readlines()
    lines = list(map(lambda x: x.strip(), lines))  # 移除斷行字元
# ===============載入檔案到變數中 end==========================

# 精確模式斷詞
tokens_1 = list(map(lambda x: list(jieba.cut(str(x), HMM=False)), lines))

# ================計算詞彙出現的次數 start========================
word_count = {}
for sent in tokens_1:  # 放入斷詞之後的變數
    for word in sent:
        if word not in word_count:
            word_count[word] = 1
        else:
            word_count[word] += 1
# ================計算詞彙出現的次數 end========================

# ================產出文字雲 start=============================
wordcloud = WordCloud(
    background_color='white',
    font_path='SourceHanSerifK-Light.otf',  # 放入中文字型檔路徑
    colormap=matplotlib.cm.cubehelix,
    width=1600,
    height=800,
    margin=2)

# wordcloud 套件 Input 需放入詞頻統計的 dict 型態變數
wordcloud = wordcloud.generate_from_frequencies(word_count)
plt.figure(figsize=(20, 10), facecolor='k')
plt.imshow(wordcloud)
plt.axis('off')
plt.tight_layout(pad=0)
plt.show()
# ================產出文字雲 end=============================
