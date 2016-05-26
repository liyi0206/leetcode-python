class Solution(object):
    def coinChange(self, coins, amount):
        """
        :type coins: List[int]
        :type amount: int
        :rtype: int
        """
        # timeout, need pruning
        # time o(mn), n=amount, m=num_coin_types
        import sys
        dp = [0]+[sys.maxint]*(amount)
        for n in range(1,amount+1):
            for m in range(len(coins)):
                if coins[m]<=n:
                    dp[n]=min(dp[n],dp[n-coins[m]]+1)
        return dp[-1] if dp[-1]<sys.maxint else -1
        
    def coinChange2(self,coins,amount):
        # time o(mn), n=amount, m=num_coin_types, but with pruning
        dp = [0]+[-1]*amount
        for x in range(amount):
            # not like real life coins, many test case has wired coin values 
            # that will make many amounts not reachable
            if dp[x]<0: continue #prune **
            for c in coins:
                if x+c>amount: continue
                if dp[x+c]<0 or dp[x+c]>dp[x]+1: dp[x+c]=dp[x]+1
        #print dp
        return dp[amount]
    
        
a=Solution()
#print a.coinChange([1,2,5],11)
#print a.coinChange([2],3)
#print a.coinChange([1,2,5],100)
print a.coinChange2([205,37,253,463,441,129,156,429,101,423,311],6653) #15
print a.coinChange2([70,177,394,428,427,437,176,145,83,370],7582) #18