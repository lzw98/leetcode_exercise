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
'''

class Solution:
    def findRepeatNumber(self, nums):
        slow=0
        fast=0
        one = [1]*len(nums)
        nums = [i+j for i,j in zip(nums,one)]
        while(1):
            slow=nums[slow]
            fast=nums[nums[fast]]
            if(slow==fast):
                break
        find=0
        while(1):
            find=nums[find]
            slow=nums[slow]
            if(find==slow):
                return find
            
a = Solution()
print(a.findRepeatNumber([0, 1, 2, 3, 4, 11, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15]))