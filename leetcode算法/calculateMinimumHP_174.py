#!/usr/bin/env python
# -*- coding:UTF-8 -*-
# AUTHOR: Zhenwei Lin
# DATE: 2020/07/12 Sun
# TIME: 10:30:46

# DESCRIPTION:

#逻辑有点小复杂，没有做出来，以后再看，逻辑有点混乱，自己没有理清楚就开始写代码了

# class Solution(object):
#     def calculateMinimumHP(self,dungeon):
#         '''
#         :type dungeon: List[List[int]]
#         :rtype: int
#         '''
#         m,n = len(dungeon),len(dungeon[0])
#         dp = [[[0,0] for _ in range(n)]for _ in range(m)]
#         # 初始化第一行与第一列
#         dp[0][0][0] = dungeon[0][0]
#         dp[0][0][1] = min(dungeon[0][0],0)
#         for i in range(1,m):
#             # 初始化第一列
#             dp[i][0][0] = dp[i-1][0][0] + dungeon[i][0]
#             dp[i][0][1] = min(dp[i-1][0][1],dp[i][0][0])
#         for i in range(1,n):
#             # 初始化第一行
#             dp[0][i][0] = dp[0][i-1][0] + dungeon[0][i]
#             dp[0][i][1] = min(dp[0][i-1][1],dp[0][i][0])
            
#         for i in range(1,m):
#             for j in range(1,n):
#                 a = dp[i-1][j][1]+dungeon[i][j]
#                 b = dp[i][j-1][1]+dungeon[i][j]
#                 val1 = dp[i-1][j][0]+dungeon[i][j]
#                 val2 = dp[i][j-1][0]+dungeon[i][j]
#                 dp[i][j][0] = val1 if dp[i-1][j][1]>dp[i][j-1][1] else val2
#                 dp[i][j][1] = min(val1,dp[i-1][j][1]) if dp[i-1][j][1]>=dp[i][j-1][1] else min(val2,dp[i][j-1][1])
                
#         return abs(dp[m-1][n-1][0]-1) if dp[m-1][n-1][0]<0 else abs(dp[m-1][n-1][1]-1)
                
class Solution:
    def calculateMinimumHP(self, dungeon):
        n,m = len(dungeon),len(dungeon[0])
        BIG = 10**9
        dp = [[BIG]*(m+1) for _ in range(n+1)]
        dp[n][m-1] = dp[n-1][m] = 1
        for i in range(n-1,-1,-1):
            for j in range(m-1,-1,-1):
                minn = min(dp[i+1][j],dp[i][j+1])
                dp[i][j] = max(minn - dungeon[i][j],1)
                # 反过来思考，假设出口的地方是1
        
        return dp[0][0]


print(Solution().calculateMinimumHP(
[[0,0,0],[1,1,-1]]))