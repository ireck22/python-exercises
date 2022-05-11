#!/usr/bin/python3.7
# -*- coding: utf-8 -*-
from ast import Str
import sys
import json
import pandas as pd
import numpy as np
import codecs
import re

strss = 'Here are UPPERCASE and lowercase chars'
finish_result = {}
x = 1

# ========== 計算每個字母出現位置 start==========
for i in strss:
    if i in finish_result:
        finish_result[i] += ','+str(x)
    else:
        finish_result[i] = str(x)
    x += 1
# ========== 計算每個字母出現位置 end===========

print(finish_result)
