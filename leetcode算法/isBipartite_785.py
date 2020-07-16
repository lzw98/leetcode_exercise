#!/usr/bin/env python
# -*- coding:UTF-8 -*-
# AUTHOR: Zhenwei Lin
# DATE: 2020/07/16 Thu
# TIME: 18:13:52

# DESCRIPTION:
class Solution:
    def isBipartite(self, graph):
        n = len(graph)
        UNCOLORED, RED, GREEN = 0, 1, 2
        color = [UNCOLORED] * n
        valid = True

        def dfs(node, c):
            nonlocal valid
            color[node] = c
            cNei = (GREEN if c == RED else RED)
            for neighbor in graph[node]:
                if color[neighbor] == UNCOLORED:
                    dfs(neighbor, cNei)
                    if not valid:
                        return
                elif color[neighbor] != cNei:
                    valid = False
                    return

        for i in range(n):
            if color[i] == UNCOLORED:
                dfs(i, RED)
                if not valid:
                    break
        
        return valid
print(Solution().isBipartite([[1,3], [0,2], [1,3], [0,2]]))
