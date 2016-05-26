class Solution(object):
    def integerBreak(self, n):
        """
        :type n: int
        :rtype: int
        """
        #If an optimal product contains a factor f >= 4, then you can replace it 
        #with factors 2 and f-2 without losing optimality, as 2*(f-2)=2f-4 >= f. 
        #So you never need a factor greater than or equal to 4, 
        #meaning you only need factors 1 (only for n=2 and n=3), 2 and 3.
        
        if n<=3: return n-1
        dp = [0]*(n+1)
        dp[2],dp[3] = 2,3
        for x in range(4, n+1):
            dp[x] = max(3*dp[x-3], 2* dp[x-2])
        return dp[n]