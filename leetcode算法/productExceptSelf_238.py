class Solution(object):
    def productExceptSelf(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        n = len(nums)
        L,R = [1]*n,[1]*n
        
        for i in range(n):
            if i == 0:
                L[0] = 1
                for _ in nums[1:n]:
                    R[0] *= _
            elif i == n-1:
                R[i] = 1
                for _ in nums[0:n-1]:
                    L[i] = L[i]*_

            else:
                for _ in nums[0:i]:
                    L[i] *= _
                for _ in nums[i+1:]:
                    R[i] *= _ 
        return [a*b for a,b in zip(L,R)]

#简化版
class Solution:
    def productExceptSelf(self, nums):
        length = len(nums)
        
        # L 和 R 分别表示左右两侧的乘积列表
        L, R, answer = [0]*length, [0]*length, [0]*length
        
        # L[i] 为索引 i 左侧所有元素的乘积
        # 对于索引为 '0' 的元素，因为左侧没有元素，所以 L[0] = 1
        L[0] = 1
        for i in range(1, length):
            L[i] = nums[i - 1] * L[i - 1]
        
        # R[i] 为索引 i 右侧所有元素的乘积
        # 对于索引为 'length-1' 的元素，因为右侧没有元素，所以 R[length-1] = 1
        R[length - 1] = 1
        for i in reversed(range(length - 1)):
            R[i] = nums[i + 1] * R[i + 1]

        # 对于索引 i，除 nums[i] 之外其余各元素的乘积就是左侧所有元素的乘积乘以右侧所有元素的乘积
        for i in range(length):
            answer[i] = L[i] * R[i]
        
        return answer

print(Solution().productExceptSelf([1,2,3,4]))