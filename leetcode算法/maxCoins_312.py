#!/usr/bin/env python
# -*- coding:UTF-8 -*-
# AUTHOR: Zhenwei Lin
# DATE: 2020/07/19 Sun
# TIME: 10:31:43

# DESCRIPTION:
from functools import lru_cache
# help(lru_cache)
class Solution:
    def maxCoins(self, nums):
        n = len(nums)
        val = [1] + nums + [1]
        
        @lru_cache(None)#缓存可以无限是这个意思吗？
        def solve(left, right):
            if left >= right - 1:
                return 0
            
            best = 0
            for i in range(left + 1, right):
                total = val[left] * val[i] * val[right]
                total += solve(left, i) + solve(i, right)
                best = max(best, total)
            
            return best

        return solve(0, n + 1)

print(Solution().maxCoins([3,1,5,8]))


## 下面是动态规划方法
# 这里面关键就是要画一画，知道算哪个dp的位置前需要算哪些位置，这样的话就知道哪些地方需要进行从后往前遍历
class Solution():
    def maxCoins(self,nums):
        n = len(nums)
        dp = [[0]*(n+2) for _ in range(n+2)]
        val = [1]+nums+[1]
        for j in range(n+2):
            for i in range(j-1,-1,-1):
                for k in range(i+1,j):
                    total = val[i]*val[k]*val[j]
                    total += dp[i][k]+dp[k][j]
                    dp[i][j] = max(dp[i][j],total)
        return dp[0][n+1]