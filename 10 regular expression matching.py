# -*- coding: utf-8 -*-
class Solution(object):
    #'.' Matches any single character.
    #'*' Matches zero or more of the preceding element.
    def isMatch(self, s, p):
        """
        :type s: str
        :type p: str
        :rtype: bool
        """
        dp=[[False]*(len(p)+1) for j in range(len(s)+1)]
        dp[0][0]=True
        for i in range(2,len(p)+1):
            if p[i-1]=='*': dp[0][i]=dp[0][i-2]
        #for l in dp: print l

        for i in range(1,len(s)+1):
            for j in range(1,len(p)+1):
                if p[j-1]!='*':
                    dp[i][j]=dp[i-1][j-1] and (s[i-1]==p[j-1] or p[j-1]=='.')
                else:
                             #skip cur and prev p
                    dp[i][j]= dp[i][j-2] or \
                             (dp[i-1][j] and \
                              (s[i-1]==p[j-2] or p[j-2]=='.'))
                             #skip cur s, while prev p == cur s, or prev p is .
        return dp[len(s)][len(p)]
        
a=Solution()
print a.isMatch("aab","c*a*b") #True