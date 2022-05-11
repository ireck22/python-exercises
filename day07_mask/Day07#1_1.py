#!/usr/bin/python3.7
# -*- coding: utf-8 -*-
import sys
import json
import requests
from bs4 import BeautifulSoup
import lxml
import pandas as pd
import numpy as np
import codecs
import re
import ssl

url = 'https://raw.githubusercontent.com/kiang/pharmacies/master/json/points.json'
res = requests.get(url)         #抓檔案
res2 = json.loads(res.text)     #json解碼

print("開始")

#json寫檔
with open("mask.json", "w", encoding='UTF-8') as f:
    f.write(json.dumps(res2, ensure_ascii=False))

print("結束")
