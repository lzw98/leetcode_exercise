class Solution:
    def longestConsecutive(self, nums):
        longsteak = 0
        num_set = set(nums)
        
        for num in num_set:      #遍历数组
            if num-1 not in num_set:  #判断前驱数是否存在
                current = num
                current_steak = 1
                while current+1 in num_set:
                    current += 1
                    current_steak += 1                    
                longsteak = max(longsteak,current_steak)
        
        return longsteak
    
print(Solution().longestConsecutive([100,4,200,1,3,2]))

                