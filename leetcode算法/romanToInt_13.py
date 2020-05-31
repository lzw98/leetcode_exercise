#!/usr/bin/env python
# -*- coding:UTF-8 -*-
# AUTHOR: Zhenwei Lin
# DATE: 2020/05/31 Sun
# TIME: 14:56:39

# # DESCRIPTION:
# digits = [(1000,'M'),(900,'CM'),(500,'D'),(400,'CD'),(100,'C'),(90,'XC'),
#                 (50,'L'),(40,'XL'),(10,'X'),(9,'IX'),(5,'V'),(4,'IV'),(1,'I')]

class Solution(object):
    def romanToInt(self, s):
        dic = {'I':1,'V':5,'X':10,'L':50,'C':100,'D':500,'M':1000}
        return sum (-dic[s[i]] if i < len(s)-1 and dic[s[i]]<dic[s[i+1]] else dic[s[i]] for i, n in enumerate(s))
    # 注意观察，要减的前一个罗马数字都比后面一个的要小
