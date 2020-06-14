#!/usr/bin/env python
# -*- coding:UTF-8 -*-
# AUTHOR: Zhenwei Lin
# DATE: 2020/06/14 Sun
# TIME: 10:45:42

# DESCRIPTION:
import bisect

class Solution:
    def findBestValue(self, arr, target):
        arr.sort()
        n = len(arr)
        prefix = [0]
        for num in arr:
            prefix.append(prefix[-1] + num)
            #获得一个排序后的列表一个一个的累加
        
        l, r, ans = 0, max(arr), -1
        while l <= r:
            mid = (l + r) // 2#求列表中极大与极小的平均值
            it = bisect.bisect_left(arr, mid)#获得这个平均值在列表中的位置
            cur = prefix[it] + (n - it) * mid#当大于这个平均值的数都变得与其一样大，得到他们的和
            if cur <= target:#如果比目标值小，说明应该增大左边值
                ans = mid
                l = mid + 1#故此处l应该从0开始枚举，而不是从列表中值最小的位置开始
            else:
                r = mid - 1#否则减小右边值

        def check(x):
            return sum(x if num >= x else num for num in arr)
        
        choose_small = check(ans)
        choose_big = check(ans + 1)
        return ans if abs(choose_small - target) <= abs(choose_big - target) else ans + 1
    
print(Solution().findBestValue(arr = [60864,25176,27249,21296,20204], target = 56808909809803))