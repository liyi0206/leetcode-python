class Solution(object):
    def isInterleave(self, s1, s2, s3):
        """
        :type s1: str
        :type s2: str
        :type s3: str
        :rtype: bool
        """
        m,n = len(s1),len(s2)
        if m+n!=len(s3): return False
        dp=[[0]*(n+1) for i in range(m+1)]
        dp[0][0]=True
        for i in range(n): dp[0][i+1]=dp[0][i] and s2[i]==s3[i]
        for i in range(m): dp[i+1][0]=dp[i][0] and s1[i]==s3[i]
        for i in range(m):
            for j in range(n):
                dp[i+1][j+1]=(dp[i][j+1] and s1[i]==s3[i+j+1]) or \
                             (dp[i+1][j] and s2[j]==s3[i+j+1])
        return dp[m][n]
        
a=Solution()
print a.isInterleave("aabcc","dbbca","aadbbcbcac") #True
print a.isInterleave("aabcc","dbbca","aadbbbaccc") #False
print a.isInterleave("","","")
print a.isInterleave("a","","a")
print a.isInterleave("aa","ab","aaba")