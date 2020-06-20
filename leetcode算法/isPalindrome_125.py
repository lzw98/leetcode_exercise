#!/usr/bin/env python
# -*- coding:UTF-8 -*-
# AUTHOR: Zhenwei Lin
# DATE: 2020/06/19 Fri
# TIME: 11:22:49

# DESCRIPTION:
class Solution(object):
    def isPalindrome(self, s):
        """
        :type s: str
        :rtype: bool
        """
        s = s.replace(':','')
        s = s.replace(' ','')
        s = s.replace(',','')
        s = s.lower()
        print(s)
        l,r = 0,len(s)-1
        while True:
            if s[l]!=s[r]:
                break
            l += 1
            r -= 1
            if l == r:
                break
        
        return True if l == r else False
    
print(Solution().isPalindrome("A man, a plan, a canal: Panama"))

