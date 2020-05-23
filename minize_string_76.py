#!/usr/bin/env python
# -*- coding:UTF-8 -*-
# AUTHOR: Zhenwei Lin
# DATE: 2020/05/23 Sat
# TIME: 23:02:25

# DESCRIPTION:
from collections import defaultdict

class Solution(object):
    def minWindow(self,s,t):
        need = defaultdict(int)
        for c in t:
            need[c] += 1
        needCnt = len(t)
        ini = 0
        res = (0,float('inf'))
        #three steps
        #first step swipe the window to contain t
        for j, c in enumerate(s):#最开始这里居然写成了t
            if need[c]>0:
                needCnt -= 1
            need[c] -= 1
        
            #second step shrink the left border until the element cannot be removed
            # and the condition is needCnt==0
            if needCnt == 0:
                while need[s[ini]]!=0:
                    need[s[ini]] += 1
                    ini += 1
                
                if j-ini<res[1]-res[0]:
                    res = (ini,j)
            #third step if this is not shortest, right window need to move to right a string 
                need[s[ini]] += 1
                needCnt += 1
                ini += 1
        return "" if res[1]>len(s) else s[res[0]:res[1]+1]


'''
class Solution(object):
    def minWindow(self, s, t):

        need = defaultdict(int)
        for c in t:
            need[c] = need[c]+1
        needCnt = len(t)
        i = 0 # i for initial position
        res = (0,float('inf')) # using two elements to record end
        # three steps
        # first swipe right to contain t 
        for j,c in enumerate(s):
            if need[c]>0:
                needCnt = needCnt-1
            need[c] = need[c] - 1
        # shrink the left border until the element cannot be removed
            if needCnt == 0:
                while True:
                    c = s[i]
                    if need[c] == 0:
                        break
                    else:
                        need[c] = need[c]+1
                        i = i+1
                if j - i < res[1] - res[0]:
                    res = (i,j)

                need[s[i]] += 1
                needCnt += 1
                i += 1
        return ""if res[1]>len(s) else s[res[0]:res[1]+1]
'''

a = Solution()
print(a.minWindow("ADOBECODEBANC","ABC"))