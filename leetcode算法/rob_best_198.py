#!/usr/bin/env python
# -*- coding:UTF-8 -*-
# AUTHOR: Zhenwei Lin
# DATE: 2020/05/29 Fri
# TIME: 09:49:23

# DESCRIPTION:

class Solution:
    def rob(self, nums):
        if not nums:
            return 0
        size = len(nums)
        if size==1:
            return nums[0]
        # use dp to denote the max money from the first i 
        dp = [0]*size
        dp[0] = nums[0]
        dp[1] = max(nums[0],nums[1])
        for i in range(2,size):
            dp[i] = max(dp[i-2]+nums[i],dp[i-1])
        
        return dp[size - 1]
