#!/usr/bin/env python
# -*- coding:UTF-8 -*-
# AUTHOR: Zhenwei Lin
# DATE: 2020/06/03 Wed
# TIME: 10:00:17

# DESCRIPTION:

class Solution(object):
    def new21Game(self, N, K, W):
        """
        :type N: int
        :type K: int
        :type W: int
        :rtype: float
        """
        #dp[x] 表示的是得分从x开始的胜率，至少要选一次，如果没有选也算失败
        if K==0:return 1.0
        dp = [0.0]*(K+W)
        for i in range(K,min(K+W-1,N)+1):
            dp[i] = 1.0
        dp[K-1] = float(min(N-K+1,W))/W
        for i in range(K-2,-1,-1):
            dp[i] = dp[i+1]-(dp[i+W+1]-dp[i+1])/W
        return dp[0] 

print(Solution().new21Game(9811,8776,1096))