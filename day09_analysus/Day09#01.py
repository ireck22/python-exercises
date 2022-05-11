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
import wget

jieba.load_userdict("dict.txt.big")

txt_file_path = "simple.txt"
# 載入檔案到變數中
with open(txt_file_path, "r", encoding='utf-8')as fn:
    lines = fn.readlines()
    lines = list(map(lambda x: x.strip(), lines))  # 移除斷行字元  字串分割

# 精確模式斷詞
tokens_1 = list(map(lambda x: list(jieba.cut(str(x), HMM=False)), lines))
print(tokens_1)
print("\n")
print("\n")

# 全模式斷詞
tokens_2 = list(
    map(lambda x1: list(jieba.cut(str(x1), cut_all=True, HMM=False)), lines))
print(tokens_2)
print("\n")
print("\n")

# 搜尋引擎模式斷詞
tokens_3 = list(
    map(lambda x2: list(jieba.cut_for_search(str(x2), HMM=False)), lines))
print(tokens_3)
