class Solution(object):        
    def numDecodings(self,s): #DP - o(1) memory
        if not s: return 0
        pp,p=0,1
        for i in range(len(s)):
            cur = 0
            if s[i]!='0': cur=p
            if i>0 and (s[i-1]=="1" or (s[i-1]=="2" and s[i] <="6")): cur+=pp
            p,pp=cur,p
        return p
      
class Solution1(object):        
    def numDecodings(self,s): #DP - o(n) memory
        if not s: return 0
        dp=[0]*len(s)
        if s[0]!='0': dp[0]=1
        for i in range(1,len(s)):
            if s[i]!='0': dp[i]=dp[i-1]
            if self.is_valid(s[i-1:i+1]): dp[i]+=dp[i-2] if i>1 else 1
        return dp[-1]
        
    def is_valid(self,s):
        if 1<=int(s)<=26 and s[0]!='0': return True
        return False
        
class Solution2(object):  
    def numDecodings(self,s): #DFS - return all possibilities
        self.res=[]
        self.bt(s,[])
        return self.res
        
    def bt(self,s,tmp):
        if not s:
            self.res.append(tmp)
            return
        if self.is_valid(s[:1]): self.bt(s[1:],tmp+[s[:1]])
        if len(s)>=2 and self.is_valid(s[:2]): self.bt(s[2:],tmp+[s[:2]])
        
    def is_valid(self,s):
        if 1<=int(s)<=26 and s[0]!='0': return True
        return False
        
a=Solution()
print a.numDecodings("10") #1
print a.numDecodings("12") #2
print a.numDecodings("00") #0
print a.numDecodings("607")#0
print a.numDecodings("4757562545844617494555774581341211511296816786586787755257741178599337186486723247528324612117156948")
##TLE #589824
