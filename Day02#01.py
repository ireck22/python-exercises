#!/usr/bin/python3.7
# -*- coding: utf-8 -*-
import sys
import json
import pandas as pd
import numpy as np
import codecs
import re


s=input("請輸入字串:")      # 輸入框
s=s.split('.')             #輸入進來時會有句點所以先把內容篩選出來
repw='good'                #要取代的字串
s2=[]
s2=s[0].split(' ')         #以空格為字串分割 

#=========== 檢查有沒有not all start===============
if ('not' in s2) and ('all' in s2):
    not_in=s2.index('not')  #找not的key值
    all_in=s2.index('all')  #找all的key值
else :
    print("no result")      #沒有的話退出程式
    sys.exit()
#=========== 檢查有沒有not all end=================

#==========字串連接，組好要取代的字串 start=========
stren=''
all_in=all_in+1
del s2[not_in:all_in]  #刪掉要取代的字串  
s2.insert(not_in,repw) #插入not的位置
#==========字串連接，組好要取代的字串 end===========

#====最後把整理好的陣列做字串連接 start=============
len=len(s2)
for i in range(0,len):
    if i==len-1:
        stren=stren+s2[i]+'.'
        break
    stren=stren+s2[i]+' '
print(stren)
#====最後把整理好的陣列做字串連接 end===============

