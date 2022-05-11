#!/usr/bin/python3.7
# -*- coding: utf-8 -*-
import sys
import json
import pandas as pd
import numpy as np
import codecs
import re


def add1(n):
    return n+1


def isPrime(n):
    if n % 2 == 1:
        return "true"
    else:
        return "false"


def f(L, F):
    result = []
    for i in L:
        result.append(F(i))
    return result


L = [1, 2, 3, 4, 5, 6]
print(L)
F = add1
L2 = f(L, F)  # 帶入要處理的陣列和function
print("每個元素加1: ", L2)

F = isPrime
L2 = f(L, F)  # 帶入要處理的陣列和function
print("判斷是否為質數: ", L2)
