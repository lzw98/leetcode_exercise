#!/usr/bin/env python
# -*- coding:UTF-8 -*-
# AUTHOR: Zhenwei Lin
# DATE: 2020/06/05 Fri
# TIME: 11:28:53

# DESCRIPTION:

class Solution:
    def spiralOrder(self, matrix):
        if not matrix or not matrix[0]:
            return []
        
        rows, columns = len(matrix), len(matrix[0])
        visited = [[False] * columns for _ in range(rows)]#建立一个是否遍历过的数组
        total = rows * columns
        order = [0] * total

        directions = [[0, 1], [1, 0], [0, -1], [-1, 0]]#从左到右，从上到下，从右到左，从下到上
        row, column = 0, 0
        directionIndex = 0
        for i in range(total):
            order[i] = matrix[row][column]
            visited[row][column] = True
            nextRow, nextColumn = row + directions[directionIndex][0], column + directions[directionIndex][1]
            if not (0 <= nextRow < rows and 0 <= nextColumn < columns and not visited[nextRow][nextColumn]):
                directionIndex = (directionIndex + 1) % 4
            row += directions[directionIndex][0]
            column += directions[directionIndex][1]
        return order

