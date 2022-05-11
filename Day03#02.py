#!/usr/bin/python3.7
# -*- coding: utf-8 -*-
import sys
import json
import pandas as pd
import numpy as np
import codecs
import re

n=input('序列:')
target=int(input('target:'))
result=n.split(',')
len=len(result)
finish_result=[]

def two_sum(result,target):
    """
    找兩個數合起來等於target\n
    result是list，target一開始輸入的
    """
    sum=0
    for i in range(0,len):
        for d in range(i+1,len):
            sum=int(result[i])+int(result[d])
            if sum==target:
                return [i,d]

result=two_sum(result,target)
print(result)

