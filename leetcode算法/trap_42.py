#!/usr/bin/env python
# -*- coding:UTF-8 -*-
# AUTHOR: Zhenwei Lin
# DATE: 2020/05/30 Sat
# TIME: 15:18:47

# DESCRIPTION:

class Solution(object):
    def trap(self, height):
        """
        :type height: List[int]
        :rtype: int
        """
        n = len(height)
        mono_stack = []
        water = 0
        for i in range(n):
            while mono_stack and height[mono_stack[-1]]<=height[i]:
                top = mono_stack.pop()
                if not mono_stack:
                    break
                water = water + (min(height[mono_stack[-1]],height[i])-height[top])*(i-mono_stack[-1]-1)
                #这地方如果有点逻辑忘记怎么写了，可以举一个小范围内的例子来看
            mono_stack.append(i)
        return water


a = Solution()
print(a.trap([0,1,0,2,1,0,1,3,2,1,2,1]))