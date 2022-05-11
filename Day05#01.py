#!/usr/bin/python3.7
# -*- coding: utf-8 -*-
import sys
import json
import pandas as pd
import numpy as np
import codecs
import re
import itertools

s = input('輸入字串')
s = sorted(set(s))  # 字典初始化和變倒敘
perm = itertools.permutations(s)  # 使用排列組合套件

# ===============整理前面排好的字串 start==============
finish = []
for i in perm:
    str_temp = ''  # 整裡字串初始化
    for d in i:
        str_temp += d  # 把每個元素的字串連起來再放到陣列

    finish.append(str_temp)
# ===============整理前面排好的字串 end==============

print(finish)
