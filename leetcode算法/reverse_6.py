#!/usr/bin/env python
# -*- coding:UTF-8 -*-
# AUTHOR: Zhenwei Lin
# DATE: 2020/05/29 Fri
# TIME: 21:59:40

# DESCRIPTION:

class Solution(object):
    def reverse(self,x):
        ans = 0 
        flag = 1 
        if x<0:
            x = -x
            flag = -1
        while x!=0:
            cur = x%10
            ans = ans*10 + cur
            x //= 10
        return ans*flag if -2**31 <ans*flag <2**31 else 0
            
            
        
