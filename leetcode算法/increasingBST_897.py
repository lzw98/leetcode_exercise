#!/usr/bin/env python
# -*- coding:UTF-8 -*-
# AUTHOR: Zhenwei Lin
# DATE: 2020/06/16 Tue
# TIME: 17:01:00

# DESCRIPTION:


# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

# class Solution:
#     def increasingBST(self, root):
#         def inorder(node):
#             if node:
#                 inorder(node.left)
#                 node.left = None
#                 self.cur.right = node
#                 self.cur = node
#                 inorder(node.right)

#         ans = self.cur = TreeNode(None)
#         inorder(root)
#         return ans.right

class Solution:
    def increasingBST(self, root):
        def inorder(node):
            if node:
                yield from inorder(node.left)
                yield node.val
                yield from inorder(node.right)

        ans = cur = TreeNode(None)
        for v in inorder(root):
            cur.right = TreeNode(v)
            cur = cur.right
        return ans.right

# def generate_tree(root,value,idx = 0):
#     if value:
#         try:
#             root.left = TreeNode(value.pop(0))
#             root.right = TreeNode(value.pop(0))
#             idx += 1
#             generate_tree(root.left,value[:idx*2],idx)
#             #这样写的话会导致不知道什么时候这个就该停止了，这样这个列表，在这里将会全部用完，而无法到下一句代码中去使用value
#             #所以这里要说明哪些是左树的数据，哪些是右树的数据
#             generate_tree(root.right,value[:idx*2],idx)#这样写也不对，这里不是一个完整的二叉树，还不能通过计算来获得左右树的数据分别是哪些
#         except:
#             return root
#     else:
#         return root

    
value = [5,3,6,2,4,None,8,1,None,None,None,7,9]
root = TreeNode(value.pop(0))
root.left = TreeNode(value.pop(0))
root.right = TreeNode(value.pop(0))
root.left.left = TreeNode(2)
root.left.left.left = TreeNode(1)
root.left.right = TreeNode(4)
root.right.right = TreeNode(8)
root.right.right.left = TreeNode(7)
root.right.right.right = TreeNode(9)

print(Solution().increasingBST(root).right.right.val)

