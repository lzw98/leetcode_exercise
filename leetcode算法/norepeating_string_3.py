#!/usr/bin/env python
# -*- coding:UTF-8 -*-
# AUTHOR: Zhenwei Lin
# DATE: 2020/05/19 Tue
# TIME: 22:56:20

# DESCRIPTION:find the substring without repeating  


class Solution(object):
    def lengthOfLongestSubstring(self, s):
        """
        :type s: str
        :rtype: int
        """
        occ = set()
        n = len(s)
        # rk is the right point, and the initial is -1. Equivalent to left of string
        # but not moving
        rk, ans = -1,0
        for i in range(n):
            # remove string from first
            if i!=0:
                occ.remove(s[i-1])
            # add unique string to occ set
            while rk+1<n and s[rk+1] not in occ:
                occ.add(s[rk+1])
                rk = rk + 1                
            ans = max(ans,rk-i+1)
        return ans
    
a = Solution()  
print(a.lengthOfLongestSubstring('abcabc'))