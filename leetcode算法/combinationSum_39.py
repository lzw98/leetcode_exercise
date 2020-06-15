#!/usr/bin/env python
# -*- coding:UTF-8 -*-
# AUTHOR: Zhenwei Lin
# DATE: 2020/06/15 Mon
# TIME: 13:41:35

# DESCRIPTION:
import copy
class Solution(object):
    def combinationSum(self, candidates, target):
        """
        :type candidates: List[int]
        :type target: int
        :rtype: List[List[int]]
        """
        #先排序
        candidates.sort()
        #定义回溯函数
        out = []
        def backtrack(ta,stack=[],index=0):
            for n,i in enumerate(candidates[index:]):                               
                if ta - i < 0:
                    break
                a = copy.deepcopy(stack)#在执行前最好先copy一下以避免变量变化对后面的影响
                a.append(i) 
                if ta - i == 0:
                    out.append(a)
                else:                    
                    backtrack(ta-i,a,index+n)
        
        backtrack(target,[])
        return out


print(Solution().combinationSum(candidates = [2,3,6,7], target = 7))
