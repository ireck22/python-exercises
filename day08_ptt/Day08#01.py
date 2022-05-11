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

# ========模擬一般使用者的情況 start================
r = requests.Session()

# 解18禁制
payload = {
    "from": "/bbs/Gossiping/index.html",
    "yes": "yes"
}

headers = {
    'user-agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_12_3) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/56.0.2924.87 Safari/537.36'
}

res = r.post("https://www.ptt.cc/ask/over18", data=payload, headers=headers)
# ========模擬一般使用者的情況的設定 end================

# ========抓兩頁的資料 start===========================
for i in range(1, 3):
    res = r.get("https://www.ptt.cc/bbs/Gossiping/index"+str(i)+".html")
    soup = BeautifulSoup(res.text, 'lxml')

    result = soup.find_all('div')                   # 先拿全部的div
    main_url = 'https://www.ptt.cc/'                # 網址前頭設定
    finish = []                                     # 放最後的結果

    for row in result:
        if row.find('div', class_='title'):          # div的class是title再進去
            title = row.find('div', class_='title')  # 先篩選title
            if title.find('a'):
                title2 = title.find('a').text        # 在進a裡拿文字
                href = title.find('a')['href']       # 拿href
                url = main_url+href                  # 還原網址

                # ======== 把文章裡的內文拿出來 start================
                res2 = r.get(url)
                soup2 = BeautifulSoup(res2.text, 'lxml')
                content = soup2.find('div', id='main-content').text
                content2 = content.split("--")[0]  # 不拿回應
                # ======== 把文章裡的內文拿出來 end================

                finish.append([title2, url, content2])  # 新增到陣列
# ========抓兩頁的資料 start===========================

# ========輸出csv start===============================
rs = pd.DataFrame(finish, columns=['title', 'url', 'content'])
rs.to_csv('content.csv')
print("end")
# ========輸出csv start===============================
