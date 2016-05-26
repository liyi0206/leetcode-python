class Solution(object):
    def numDistinct(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: int
        """
        if not s: return 0
        if not t: return 1
        res=[1]+[0]*len(t)
        for i in range(len(s)):
            for j in range(len(t)-1,-1,-1):
                print i,j
                if s[i]==t[j]: res[j+1]=res[j]+res[j+1];print res
                #else: res[j+1]=res[j+1]
        return res[-1]
        
    def numDistinct2(self,s,t):
        m,n = len(s),len(t)
        dp=[[0]*(n+1) for i in range(m+1)]
        for i in range(m+1): dp[i][0]=1
        for i in range(1,m+1):
            for j in range(1,n+1):
                if s[i-1]==t[j-1]: dp[i][j]=dp[i-1][j-1]+dp[i-1][j]
                else: dp[i][j] = dp[i-1][j]
        #for l in dp: print l
        return dp[m][n]
        
a=Solution()
print a.numDistinct2("rabbbit","rabbit") #3