#!/usr/bin/env python
# -*- coding:UTF-8 -*-
# AUTHOR: Zhenwei Lin
# DATE: 2020/05/29 Fri
# TIME: 15:44:12

# DESCRIPTION:
class Solution(object):
    def findNumberIn2DArray(self, matrix, target):
        """
        :type matrix: List[List[int]]
        :type target: int
        :rtype: bool
        """
        try:
            n,m = len(matrix),len(matrix[0])
            if m == 0 or n == 0:
                return False
        except:
            return False
        index_col_left = m-1
        index_row_left= n-1
        index_col_right = 0
        index_row_right = 0
        for i in range(m):
            if matrix[0][i]>=target:
                if matrix[0][i]==target:
                    return True
                index_col_left = min(index_col_left,i)
            else:
                index_col_right = max(index_col_right,i)
        for i in range(n):
            if matrix[i][0]>=target:
                if matrix[i][0] == target:
                    return True
                index_row_left = min(index_row_left,i)
            else:
                index_row_right = max(index_row_right,i)
        
        if matrix[index_row_left][index_col_left]>=target:
            if index_col_right<=index_col_left and index_row_right<=index_row_left:
                return True            
        else:
            return False


        
        


        
        
        


a = Solution()
print(a.findNumberIn2DArray([[1,4],[2,5]],5))
