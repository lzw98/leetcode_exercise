#!/usr/bin/env python
# -*- coding:UTF-8 -*-
# AUTHOR: Zhenwei Lin
# DATE: 2020/05/26 Tue
# TIME: 11:22:02

# DESCRIPTION: fast and slow index

# Definition for singly-linked list.

class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution(object):
    def detectCycle(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        fast,slow = head,head
        begin = head
        count = 0
        while True:            
            try:
                slow = slow.next
                fast = fast.next.next
            except:
                return None
            if slow == fast:
                encounter = slow
                break
            if fast == None:
                return None

        while True:
            if begin == encounter:
                return begin
            begin = begin.next
            encounter = encounter.next
            count += 1


