# -*- coding: utf-8 -*-
class Solution:
    #'?' Matches any single character.
    #'*' Matches any sequence of characters (including the empty sequence).
    def isMatch(self, s, p):
        """
        :type s: str
        :type p: str
        :rtype: bool
        """
        a, b, lasta, lastb = 0, 0, -1, -1
        while a<len(s):
            if b<len(p) and (s[a]==p[b] or p[b]=='?'): a,b = a+1,b+1
            elif b<len(p) and p[b]=='*':
                b = b+1
                lastb,lasta = b,a
            elif lastb != -1:
                lasta = lasta+1
                b,a = lastb,lasta
            else: return False
        while b<len(p) and p[b]=='*': b=b+1
        return b == len(p)
        
    def isMatch1(self, s, p): #DP - AC, which I don't understand 
        length = len(s)
        if len(p)-p.count('*')>length: return False
        dp = [True]+[False]*length
        for x in p:
            if x!='*':
                for n in reversed(range(length)):
                    dp[n+1]= dp[n] and (x==s[n] or x=='?')
            else:
                for n in range(1,length+1): 
                    dp[n]=dp[n-1] or dp[n]
            dp[0]= dp[0] and x=='*'
        return dp[-1]
    
    def isMatch2(self, s, p): # DP - TLE
        dp=[[False]*(len(p)+1) for j in range(len(s)+1)]
        dp[0][0]=True
        for i in range(2,len(p)+1):
            if p[i-1]=='*': dp[0][i]=dp[0][i-2]
        #for l in dp: print l
                    
        for i in range(1,len(s)+1):
            for j in range(1,len(p)+1):
                if p[j-1]!='*':
                    dp[i][j]=dp[i-1][j-1] and (s[i-1]==p[j-1] or p[j-1]=='?')
                else:
                    dp[i][j]= dp[i][j-1] or dp[i-1][j-1]
        return dp[len(s)][len(p)]
        
a=Solution()
print a.isMatch("aab","*a*b") #True