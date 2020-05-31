#!/usr/bin/env python
# -*- coding:UTF-8 -*-
# AUTHOR: Zhenwei Lin
# DATE: 2020/05/31 Sun
# TIME: 09:47:17

# DESCRIPTION:

# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None
#左节点的左右，右节点的左右
class Solution(object):
    def isSymmetric(self, root):
        """
        :type root: TreeNode
        :rtype: bool
        """
        def symm(left,right):
            if left == None and right==None:return True
            if left == None or right == None:return False
            if left.val != right.val: return False
            else: return symm(left.left,right.right) and symm(left.right,right.left)

        while True:
            if root == None:
                return True
            
            else:
                return symm(root.left,root.right)
            
            
            
# [1,2,2,3,4,4,3]
