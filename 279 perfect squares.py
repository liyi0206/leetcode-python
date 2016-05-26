class Solution(object):
    def numSquares(self, n):#forward - timeout
        """
        :type n: int
        :rtype: int
        """
        import math
        dp = [0]+[-1]*n
        squares=[i**2 for i in range(1,int(math.sqrt(n))+1)]
        for x in range(n):
            #if dp[x]<0: continue
            for c in squares:
                if x+c>n: continue
                if dp[x+c]<0 or dp[x]+1<dp[x+c]: dp[x+c]=dp[x]+1
        #print dp
        return dp[n]
        
    def numSquares2(self, n):#backward - timeout
        import sys
        import math
        dp = [0]+[sys.maxint]*(n)
        squares=[i**2 for i in range(1,int(math.sqrt(n))+1)]
        for n in range(1,n+1):
            for m in range(len(squares)):
                if squares[m]<=n:
                    dp[n]=min(dp[n],dp[n-squares[m]]+1)
            #print "dp",n,dp[n]
        return dp[-1] if dp[-1]<sys.maxint else -1

class Solution2(object):
    _dp = [0]   
    def numSquares3(self, n):#backward - accepted
        # 1, dp = self._dp - don't know why but if not TLE
        # 2, only consider the square roots <len(dp) at cur
        dp = self._dp
        while len(dp)<=n: #dp[i] for number i
            # valid roots up till number i, which is len(dp)
            valid_roots=range(1,int(len(dp)**0.5+1)) 
            dp.append(min(dp[-i*i] for i in valid_roots)+1)
        return dp[n]


a=Solution()
print a.numSquares(12) #3
print a.numSquares(13) #2
print a.numSquares(8829) #2
print a.numSquares(9975) #4