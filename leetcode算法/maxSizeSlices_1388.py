#!/usr/bin/env python
# -*- coding:UTF-8 -*-
# AUTHOR: Zhenwei Lin
# DATE: 2020/06/18 Thu
# TIME: 15:03:21

# DESCRIPTION:

class Solution(object):
    def maxSizeSlices(self, slices):
        """
        :type slices: List[int]
        :rtype: int
        """
        def get_index(s,a,b,n):
            if a>b:
                return s[b:a]
            else:
                return s[0:a]+s[b:]
        def backtrack(s):
            n = len(s)
            if n == 3:
                return max(s)
            else:
                return max(x+backtrack(get_index(s,(i-1)%n,(i+2)%n,n)) for i,x in enumerate(s))
        ans = backtrack(slices)
        return ans
    
print(Solution().maxSizeSlices([4,1,2,5,8,3,1,9,7]))

# def backtrack(s):
#     return max(s)
# x = 9
# i = 4
# slice = [8,9,8,6,1,1]
# print((i+2)%6,(i-1)%6)

#如果(i+2)%n>(i-1)%n:则正常
#如果(i+2)%n<(i-1)%n:则取补

'''
以上自己写的算法会超出时间限制，下面给出官方的动态规划的解答
'''

class Solution:
    def maxSizeSlices(self, slices):
        def calculate(s):
            n = len(s)
            choose = (n + 1) // 3
            dp = [[0] * (choose + 1) for _ in range(n + 1)]
            for i in range(1, n + 1):
                for j in range(1, choose + 1):
                    dp[i][j] = max(dp[i - 1][j], (dp[i - 2][j - 1] if i - 2 >= 0 else 0) + s[i - 1])
            return dp[n][choose]
        #dp[i][j]表示的是在前i个数中选择了j个不相邻的数的最大和
        #因此分成选择了第i个数与不选择第i个数两种情况进行讨论，比较选择较大的数
        ans1 = calculate(slices[1:])
        ans2 = calculate(slices[:-1])
        #上面讨论的是非环状序列的情况，如果是环状序列，相较于普通序列，相当于添加了一个限制，普通序列中的第一个和最后一个数不能同时选，这样我们只需要对普通序列进行两遍动态规划就好了，分别删除第一个数与最后一个数进行动态规划。
        return max(ans1, ans2)
