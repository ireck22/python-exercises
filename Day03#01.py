#!/usr/bin/python3.7
# -*- coding: utf-8 -*-
import sys
import json
import pandas as pd
import numpy as np
import codecs
import re

a=input("input a:")
b=input("input b:")
int_a,int_b=int(a),int(b)

# 當a大於b時就對調
if int_a>int_b:
    int_a=int_b
    int_b=int_a

# 這個是用來檢查該數字是不是自除數
def check_slave(i):
    res_int=str(i)              #數字轉字串
    res_array=list(res_int)     #數字字串轉成list
    for row in res_array:
        row_int=int(row)
        if row_int==0:          #數字的個別數是0話就回傳false
            return False
        elif i % row_int!=0:    #數字的個別數不整除話就回傳false
            return False
    return True                 #檢查ok後回傳true

#============ 整理自除數 start=========================
int_b+=1
result=[]
for i in range(int_a,int_b):
    if check_slave(i):
        result.append(i)
#============ 整理自除數 end===========================

#============找出差異最大的前後兩位 start===============
length=len(result)
if length>0:            #有自除數在做尋找
    max=0               #最大差異數初始化
    
    for idx in range (1,length):
        max_idx=result[idx]-result[idx-1]
        if max_idx>max:
            max=max_idx
            res_idx=idx     #放索引

    print([result[res_idx-1],result[res_idx]])
else:
    print("沒有自除數")
#============找出差異最大的前後兩位 end===============
