#!/usr/bin/env python
# -*- coding:UTF-8 -*-
# AUTHOR: Zhenwei Lin
# DATE: 2020/06/17 Wed
# TIME: 10:52:21

# DESCRIPTION:

class Solution(object):
    def maxScoreSightseeingPair(self, A):
        """
        :type A: List[int]
        :rtype: int
        """
        res = 0
        mx = 0
        for i in range(len(A)-1):
            mx = mx if mx>A[i] + i else A[i] + i
            r = mx + A[i+1] - i-1
            #加一的操作就避免了其造成第一个地方就会出现重复位置
            res = r if r>res else res
        return res
    
    
print(Solution().maxScoreSightseeingPair([8,1,5,2,6]))
