#!/usr/bin/env python
# -*- coding:UTF-8 -*-
# AUTHOR: Zhenwei Lin
# DATE: 2020/05/29 Fri
# TIME: 10:03:19

# DESCRIPTION:

#下面这种写法就陷入死循环了，有闭环
'''
class Solution(object):
    def findRepeatNumber(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        fast,slow = 0,0
        while True:
            if nums[fast] == nums[slow] and fast != 0:
                return nums[fast]

            fast = nums[nums[fast]]
            slow = nums[slow]
'''

class Solution(object):
    def findRepeatNumber(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        dct = {}
        for i in nums:
            try:
                if dct[i]:
                    dct[i] += 1
            except:
                dct[i] = 1
        d = [k for k,v in dct.items() if v>1]
        return d[0]


            
a = Solution()
print(a.findRepeatNumber([0, 1, 2, 3, 4, 11, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15]))