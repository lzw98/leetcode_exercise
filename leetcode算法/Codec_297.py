#!/usr/bin/env python
# -*- coding:UTF-8 -*-
# AUTHOR: Zhenwei Lin
# DATE: 2020/06/16 Tue
# TIME: 09:10:04

# DESCRIPTION:


# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Codec:

    def serialize(self, root): # 要求转化成字符串格式
        def dfs(root):
            if not root:
                return 'null,'
    
            left = dfs(root.left)
            right = dfs(root.right)

            return str(root.val) + ',' + left + right

        return dfs(root)
        

    def deserialize(self, data):
        def dfs(data):
            try:
                val = data.pop(0)
            except:
                return None

            if val == 'null':
                return None
            
            node = TreeNode(val)
            node.left = dfs(data)#先左树进行了一次pop，这样再进行右树的时候就少了一个元素
            node.right = dfs(data)

            return node

        dataList = data.split(',') # 上一个函数得到的字符串序列转化为数组
        return dfs(dataList)
    



# Your Codec object will be instantiated and called as such:
codec = Codec()
print(codec.serialize(codec.deserialize('1,2,3,null,null,4,5')))
