#!/usr/bin/python3.7
# -*- coding: utf-8 -*-
import sys
import json
from matplotlib.cbook import safe_masked_invalid
import pandas as pd
import numpy as np
import codecs
import re

# 當n是0和1時就回傳1
# 不是這兩個數時進行遞迴計算，也就是把前兩個數加起來再回傳


def climb(n):
    if n == 0:
        return 1
    elif n == 1:
        return 1

    sum = climb(n-1)+climb(n-2)
    return sum


n = input("輸入:")
result = climb(int(n))
print(result)
