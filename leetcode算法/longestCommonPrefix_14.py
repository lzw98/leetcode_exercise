#!/usr/bin/env python
# -*- coding:UTF-8 -*-
# AUTHOR: Zhenwei Lin
# DATE: 2020/06/01 Mon
# TIME: 10:16:25

# DESCRIPTION:

class Solution(object):
    def longestCommonPrefix(self, strs):
        """
        :type strs: List[str]
        :rtype: str
        """
        s = []
        n = len(strs)
        if not strs: return ""
        if n==1 :return strs[0]    
        
        for i in range(min(len(_) for _ in strs)):
            flag = 1
            for j in range(n):
                if strs[j][i] == strs[j-1][i]:
                    flag = flag * 1
                else:
                    flag = flag*0
            if flag:
                s.append(strs[0][i])
            else:
                break
        
        return "".join(s)
    
print(Solution().longestCommonPrefix(["aca","cba"]))
