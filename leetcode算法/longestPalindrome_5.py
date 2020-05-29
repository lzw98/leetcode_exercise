#!/usr/bin/env python
# -*- coding:UTF-8 -*-
# AUTHOR: Zhenwei Lin
# DATE: 2020/05/29 Fri
# TIME: 21:33:30

# DESCRIPTION:

class Solution:
    def longestPalindrome(self, s):
        n = len(s)
        dp = [[False] * n for _ in range(n)]
        ans = ""
        # 枚举子串的长度 l+1
        for l in range(n):
            # 枚举子串的起始位置 i，这样可以通过 j=i+l 得到子串的结束位置
            for i in range(n):
                j = i + l#这里是l 不是1
                if j >= n:
                    break
                if l == 0:
                    dp[i][j] = True
                elif l == 1:
                    dp[i][j] = (s[i] == s[j])
                else:
                    dp[i][j] = (dp[i + 1][j - 1] and s[i] == s[j])
                if dp[i][j] and l + 1 > len(ans):
                    ans = s[i:j+1]
        return ans
    
a = Solution()
a.longestPalindrome("babad")
