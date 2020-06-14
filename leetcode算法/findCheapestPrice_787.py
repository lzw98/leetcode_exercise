#!/usr/bin/env python
# -*- coding:UTF-8 -*-
# AUTHOR: Zhenwei Lin
# DATE: 2020/06/14 Sun
# TIME: 14:21:53

# DESCRIPTION:
import collections
import copy
class Solution(object):
    def findCheapestPrice(self, n, flights, src, dst, K):
        """
        :type n: int
        :type flights: List[List[int]]
        :type src: int
        :type dst: int
        :type K: int
        :rtype: int
        """
        dct = collections.defaultdict(list)
        for u,v,w in flights:
            dct[v].append((u,w))

        out = []
        def backtrack(station,s = []):
            s.append(station)
            if station == src:
                a = copy.deepcopy(s)
                out.append(a)
            else:
                m = dct.get(station)
                try:
                    for sta in dct.get(station):
                        # s.append(station) 这句放在这里的话，会产生一定的问题，前面的运行递归会对后面产生影响                    
                        a = copy.deepcopy(s)
                        backtrack(sta[0],a)
                except:
                    pass
                    
        backtrack(dst,[])
        res = [r for r in out if len(r) == K+2]
        # return dct
        if not res:
            return -1
        
        def cal_fee(route):
            fee = 0
            for i,s in enumerate(route):
                if s == 0:
                    return fee
                else:
                    f = dct[s]
                    for en in f:
                        if en[0] == route[i+1]:
                            fee += en[1]
        money = [cal_fee(rou) for rou in res]
        return min(money)


class Solution(object):
    def findCheapestPrice(self, n, flights, src, dst, K):
        dist = [[float('inf')] * n for _ in range(2)]
        dist[0][src] = dist[1][src] = 0

        for i in range(K+1):
            for u, v, w in flights:
                dist[i&1][v] = min(dist[i&1][v], dist[~i&1][u] + w)

        return dist[K&1][dst] if dist[K&1][dst] < float('inf') else -1
        
            
print(Solution().findCheapestPrice(5,[[4,1,1],[1,2,3],[0,3,2],[0,4,10],[3,1,1],[1,4,3]],2,1,1))
