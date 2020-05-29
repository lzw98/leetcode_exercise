#!/usr/bin/env python
# -*- coding:UTF-8 -*-
# AUTHOR: Zhenwei Lin
# DATE: 2020/05/25 Mon
# TIME: 10:16:37

# DESCRIPTION:can pass the test, but waste too much cache

class Solution(object):
    def maxArea(self, height):
        """
        :type height: List[int]
        :rtype: int
        """
        index1, index2 = 0,len(height)-1
        capacity = 0
        while True:
            if index1 == index2:
                return capacity
            
            l = index2 - index1
            h = min(height[index1],height[index2])
            if capacity < (l*h):
                capacity = l*h
                
            if height[index1]<height[index2]:
                index1 += 1
            else:
                index2 -= 1
