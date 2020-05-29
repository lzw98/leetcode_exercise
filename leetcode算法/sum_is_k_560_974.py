# #!/usr/bin/env python
# # -*- coding:UTF-8 -*-
# # AUTHOR: Zhenwei Lin
# # DATE: 2020/05/27 Wed
# # TIME: 10:25:50

# # DESCRIPTION:
'''
class Solution(object):
    def subarraySum(self, A, K):
        #前缀和加取模运算加哈希;注意python是向下取整的
        hashmap = {0:1}
        presum = 0
        count = 0
        for i in range(len(A)):
            presum = (presum + A[i])
            if presum-K in hashmap:
                count += hashmap[presum-K]
            if hashmap.get(presum):
                hashmap[presum] += 1
            else:
                hashmap[presum] = 1
            # print(hashmap)
        return count
    
'''

class Solution:
    def subarraysDivByK(self, A, K):
        #前缀和加取模运算加哈希;注意python是向下取整的
        hashmap = {0:1}
        presum = 0
        count = 0
        for i in range(len(A)):
            presum = (presum + A[i]) % K
            if presum in hashmap:# if get the same remainder means that the new subarray is integer multiple of K.
                count += hashmap[presum]
            if hashmap.get(presum):
                hashmap[presum] += 1
            else:
                hashmap[presum] = 1
            # print(hashmap)
        return count

a = Solution()
print(a.subarraysDivByK([4,5,0,-2,-3,1], 5))