#!/usr/bin/env python
# -*- coding:UTF-8 -*-
# AUTHOR: Zhenwei Lin
# DATE: 2020/05/22 Fri
# TIME: 19:51:38

# define nodetree

class TreeNode(object):
    def __init__(self,x):
        self.val = x
        self.left = None
        self.right = None

class Solution(object):
    def buildTree(self, preorder, inorder):
        """
        :type preorder: List[int]
        :type inorder: List[int]
        :rtype: TreeNode
        """
        if not preorder or not inorder: # 记住 not null or not null 说明其中一个非空则return
            return
        root = TreeNode(preorder[0])
        idx = inorder.index(preorder[0])
        
        root.left = self.buildTree(preorder[1:idx+1],inorder[:idx])
        root.right = self.buildTree(preorder[1+idx:],inorder[idx+1:])
        
        return root
    
a = Solution()
b = a.buildTree(preorder = [3,9,20,15,7],inorder = [9,3,15,20,7])
