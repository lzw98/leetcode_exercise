#!/usr/bin/env python
# -*- coding:UTF-8 -*-
# AUTHOR: Zhenwei Lin
# DATE: 2020/06/01 Mon
# TIME: 09:36:57

# DESCRIPTION:

class Solution(object):
    def kidsWithCandies(self, candies, extraCandies):
        """
        :type candies: List[int]
        :type extraCandies: int
        :rtype: List[bool]
        """
        n = len(candies)
        ans = [True]*n
        maximum = max(candies)
        for i,candy in enumerate(candies):
            if (candy+extraCandies)>=maximum:
                ans[i]=True
            else:
                ans[i]=False
        return ans
                
                
    
