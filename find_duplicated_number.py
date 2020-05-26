#!/usr/bin/env python
# -*- coding:UTF-8 -*-
# AUTHOR: Zhenwei Lin
# DATE: 2020/05/26 Tue
# TIME: 11:22:02

# DESCRIPTION: fast and slow index
#将列表上的数当成是指针，注意这里的定义是上面的数是不会超过数组的长度的
class Solution:
    def findDuplicate(self, nums):
        slow=0
        fast=0
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
