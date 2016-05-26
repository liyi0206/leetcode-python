# -*- coding: utf-8 -*-
class Solution(object):
    def maxProfit(self, k, prices):
        """
        :type k: int
        :type prices: List[int]
        :rtype: int
        """
        size = len(prices)
        if k>size/2: return self.quickSolve(size, prices)
        dp = [0]+[None]*(2*k)
        for i in range(size):
            #assuming at time i there is the jth transaction
            for j in range(1, min(2*k,i+1)+1):
                dp[j] = max(dp[j], dp[j-1]+prices[i]*[1,-1][j%2])
        return max(dp)

    def quickSolve(self, size, prices):
        sum = 0
        for x in range(size-1): sum+=max(0,prices[x+1]-prices[x])
        return sum