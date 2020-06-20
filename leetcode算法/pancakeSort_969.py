#!/usr/bin/env python
# -*- coding:UTF-8 -*-
# AUTHOR: Zhenwei Lin
# DATE: 2020/06/20 Sat
# TIME: 10:23:36

# DESCRIPTION:

class Solution(object):
    def pancakeSort(self, A):
        """
        :type A: List[int]
        :rtype: List[int]
        """
        ans = []
        n = len(A)
        def rev(s):
            index1 = s.index(max(s))
            media = s[:index1+1]
            media.reverse()
            s = media + s[index1+1:]
            s.reverse()
            l = len(s)
            return index1+1,l,s
        for i in range(n):
            index,l,A = rev(A)
            A.pop(-1)
            ans.append(index)
            ans.append(l)
        return ans

# class Solution(object):
#     def pancakeSort(self, A):
#         ans = []

#         N = len(A)
#         B = sorted(range(1, N+1), key = lambda i: -A[i-1])
#         for i in B:
#             for f in ans:
#                 if i <= f:
#                     i = f+1 - i
#             ans.extend([i, N])
#             N -= 1

#         return ans

