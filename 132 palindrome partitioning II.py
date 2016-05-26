class Solution(object):
    def minCut(self, s): # 2 DPs
        """
        :type s: str
        :rtype: int
        """
        n=len(s)
        dp=[[False]*n for i in range(n)] #isPalin
        res=[-1]*(n+1) #minCut
        for i in range(n): dp[i][i]=True
        for i in range(n-1,-1,-1):
            res[i]=res[i+1]+1
            for j in range(i+1,n):
                if s[i]==s[j] and (j==i+1 or dp[i+1][j-1]==True):
                    dp[i][j]=True
                    if j==n-1: res[i]=0
                    res[i]=min(res[i],res[j+1]+1)
        return res[0]
        
class Solution2(object): 
    def minCut(self,s): # 1 DP better
        N = len(s)
        dp = [i for i in range(N)]
        
        for n in range(N):
            m=0  # n is the mid
            while n-m>=0 and n+m<N and s[n-m]==s[n+m]:
                dp[n+m] = min(dp[n+m],dp[n-m-1]+1 if n-m-1>=0 else 0)  ###
                m+=1
            
            m=0 # n and n+1 are mid
            while n-m>=0 and n+1+m<N and s[n-m]==s[n+1+m]:
                dp[n+1+m] = min(dp[n+1+m],dp[n-m-1]+1 if n-m-1>=0 else 0)###
                m+=1
        return dp[-1]

a=Solution2()
print a.minCut("aab") #1
print a.minCut("abbab") #1
print a.minCut("cdd") #1
print a.minCut("cabababcbc")