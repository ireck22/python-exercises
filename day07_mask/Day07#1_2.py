#!/usr/bin/python3.7
# -*- coding: utf-8 -*-
import sys
import json
import csv
import requests
from bs4 import BeautifulSoup
import lxml
import pandas as pd
import numpy as np
import codecs
import re
import ssl
from collections import defaultdict

result = defaultdict(int)
# ====================讀取檔案 start===============================
with open('mask.json', encoding='UTF-8') as file:
    data = json.load(file)
# ====================讀取檔案 end=================================

# =================各縣市的存量 start==============================
for row in data['features']:
    county = row['properties']['county']
    if county != '':
        result[county] += 1
# =================各縣市的存量 end=================================

# ==========算每個地區的剩餘口罩數量(分成人的和小孩的) start==========
child_count = defaultdict(int)
adult_count = defaultdict(int)

for row in data['features']:
    county = row['properties']['county']
    if county != '':
        child_count[county] += row['properties']['mask_child']  # 大人的口罩
        adult_count[county] += row['properties']['mask_adult']  # 小孩的口罩

chiled_sort = sorted(child_count.items(), key=lambda kv: kv[1], reverse=True)
print("小孩口罩數量:", chiled_sort)

adult_sort = sorted(adult_count.items(), key=lambda kv: kv[1], reverse=True)
print("成人口罩數量:", adult_sort)
# ==========算每個地區的剩餘口罩數量(分成人的和小孩的) end==========

# ===================METHOD2 start================================
properties = []

for info in data['features']:
    properties += [info['properties']]

properties = pd.DataFrame(properties)
adult = properties[["county", "mask_adult"]]

# groupby分組、sum加總、mask_adult大到小排序
adult_sort = adult.groupby("county").sum().sort_values(
    by='mask_adult', ascending=False)
print(adult_sort)

child = properties[["county", "mask_child"]]
child_sort = child.groupby("county").sum().sort_values(
    by='mask_child', ascending=False)
print(child_sort)

finish_result = [adult_sort, child_sort]
finish = pd.concat(finish_result)
print("合併:", finish)
# ==============METHOD2 end=============================================
