class Solution(object):
    def minimumTotal(self, triangle):
        """
        :type triangle: List[List[int]]
        :rtype: int
        """
        dp = [0]*len(triangle)
        dp[0] = triangle[0][0]
        for i in range(1,len(triangle)):
            for j in range(i,-1,-1):
                if j == 0:
                    dp[0] = dp[0]+triangle[i][0]
                elif j==i:
                    dp[j] = dp[j-1]+triangle[i][j]
                else:
                    dp[j] = min(dp[j],dp[j-1])+triangle[i][j]
        
        return min(dp)
    
    
print(Solution().minimumTotal([
     [2],
    [3,4],
   [6,5,7],
  [4,1,8,3]
]))