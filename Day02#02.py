#!/usr/bin/python3.7
# -*- coding: utf-8 -*-
import sys
import json
import pandas as pd
import numpy as np
import codecs
import re

#=================多個輸入的 start===================
n=int(input())
result=[]
finish_result={}
for _ in range(0, n):
    d={}
    for i in range(0,2):
        name, number = input().split()
        d[name] = number
    result.append(d) #新增一維兩個元素
#=================多個輸入的 start===================

# ================兩層迴圈解法 start=================
# for i in result:
#     for key,value in i.items():
#         # print(key,value)
#         finish_result[key]=value
# print(finish_result)
# ================兩層迴圈解法 end===================

# ================update版本 start===============
for i in range(1,len(result)):
    result[0].update(result[i])
print(result[0])
# ================update版本 end===============
