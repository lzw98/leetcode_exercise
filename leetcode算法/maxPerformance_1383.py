#!/usr/bin/env python
# -*- coding:UTF-8 -*-
# AUTHOR: Zhenwei Lin
# DATE: 2020/06/17 Wed
# TIME: 18:20:59

# DESCRIPTION:
'''
我们可以枚举效率的最小值，在所有效率大于e_min的工程师中选取不超过k-1个，让他们的速度和最大（为什么是k-1而不是k个，因为最小值代表的那个工程师是必选的，加起来一共是k个）

如何选取效率大于e_min中速度最大的K-1个，如果，效率大于e_min的元素小于k-1,就全取
具体地，我们可以对工程师先按照效率从高到低排序，然后从前往后枚举这个序列中的元素作为e_min，这样可以保证前面元素的效率都比当前这个工程师高，然后维护一个以速度为关键字的小根堆，存放前面已经枚举过的元素中速度前k-1大的，动态维护这个堆的速度和。（为什么选取小取堆?因为我们要动态维护前k-1大的元素，当堆内的元素超过k-1的时候，我们可以从堆顶pop掉比较小的元素，保证最大的k-1个元素还在堆内。）
'''
import heapq
class Solution:
    class staff:
        def __init__(self,s,e):
            self.s = s
            self.e = e
        def __lt__(self, that):#通过这个类就可以进行比较（<），并且符合<则返回True
            return self.s < that.s
        
    def maxPerformance(self, n, speed, efficiency, k):
        v = [0]*n
        for i in range(n):
            v[i] = Solution().staff(speed[i],efficiency[i])
        v.sort(key = lambda x:-x.e)
        #按照-e进行排列，说明是从效率从高到低排列
        #将e从高到低进行枚举
        q = []#维护一个小根堆
        ans = 0
        totals = 0
        for i in range(n):
            minE = v[i].e
            totals = totals + v[i].s
            ans = max(ans,minE*totals)
            heapq.heappush(q,v[i])#定义了__lt__方法，这边才可以进行比较
            if len(q) == k:
                item = heapq.heappop(q)#将最小的pop出来
                totals -= item.s
        return ans%(10**9+7)
        
        
        
print(Solution().maxPerformance(n = 6, speed = [2,10,3,1,5,8], efficiency = [5,4,3,9,7,2], k = 2))