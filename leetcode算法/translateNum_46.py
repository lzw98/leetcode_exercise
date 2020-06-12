class Solution(object):
    def translateNum(self, num):
        """
        :type num: int
        :rtype: int
        """
        s = str(num)
        dp = [0]*len(s)
        dp[0] = 1
        dp[1] = (2 if '10'<=s[0:2]<='25' else 1)#初值又给搞错了啊
        for i in range(2,len(s)):
            dp[i] = (dp[i-1]+dp[i-2] if '10'<=s[i-1:i+1]<='25' else dp[i-1])
        return dp[-1]
        


print(Solution().translateNum(12258))
            
            
            