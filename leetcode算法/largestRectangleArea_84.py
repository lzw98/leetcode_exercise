#!/usr/bin/env python
# -*- coding:UTF-8 -*-
# AUTHOR: Zhenwei Lin
# DATE: 2020/05/30 Sat
# TIME: 14:11:04

# DESCRIPTION:

class Solution(object):
    def largestRectangleArea(self, heights):
        """
        :type heights: List[int]
        :rtype: int
        """
        n = len(heights)
        left,right = [0]*n,[0]*n
        mono_stack = []
        for i in range(n):
            while mono_stack and heights[mono_stack[-1]]>=heights[i]:
                mono_stack.pop(-1)
            left[i] = mono_stack[-1] if mono_stack else -1
            mono_stack.append(i)
        #上面这段代码考虑一下：假设有三个高度相同的连在一起,只留下最先进去的那个相同高度的
        
        mono_stack = []
        for i in range(n-1,-1,-1):
            while mono_stack and heights[mono_stack[-1]]>=heights[i]:
                mono_stack.pop(-1)
            right[i] = mono_stack[-1] if mono_stack else n
            mono_stack.append(i)
            
        ans = max((right[i]-left[i]-1)*heights[i] for i in range(n)) if n>0 else 0
        return ans 
        

a = Solution()
print(a.largestRectangleArea([1,1,1,4,4,4,5,6]))
