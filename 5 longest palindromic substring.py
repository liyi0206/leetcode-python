class Solution(object):
    def longestPalindrome(self, s): #naive, o(n^3) TLE
        """ 
        :type s: str
        :rtype: str
        """
        res=""
        for i in range(len(s)):
            for j in range(i,len(s)):
                if self.isPalindrome(s[i:j+1]) and len(res)<j-i+1: 
                    res=s[i:j+1]
        return res
        
    def isPalindrome(self,s):
        for i in range(len(s)/2):
            if s[i]!=s[-i-1]: return False
        return True

class Solution2(object): #o(n^2) TLE - better to check from middle to two sides,
    def longestPalindrome(self,s): # so stop early if resLen_1side*2<maxPal
        self.s=s
        start,end=0,0
        for i in range(len(s)):
            len1=self.expandAroundCenter(i,i)
            len2=self.expandAroundCenter(i,i+1)
            l=max(len1,len2)
            if l>end-start:
                start=i-(l-1)/2
                end=i+l/2
        return self.s[start:end+1]
        
    def expandAroundCenter(self,l,r): #o(n)
        while l>=0 and r<len(self.s) and self.s[l]==self.s[r]:
            l,r =l-1,r+1
        return r-l-1
        
class Solution3(object): #o(n^2) - best
    # when increase s 1 char, could only increase maxPalLen by 1 or 2, 
    # and new maxPal includes new char
    def longestPalindrome(self,s):
        if len(s)==0: return 0
        maxLen=1
        start=0
        for i in xrange(len(s)): #o(n)
            if i-maxLen >=1 and s[i-maxLen-1:i+1]==s[i-maxLen-1:i+1][::-1]:
                start=i-maxLen-1
                maxLen+=2
                continue

            if i-maxLen >=0 and s[i-maxLen:i+1]==s[i-maxLen:i+1][::-1]:
                start=i-maxLen
                maxLen+=1
        return s[start:start+maxLen]
        
a=Solution()
print a.longestPalindrome3("a")
print a.longestPalindrome3("bb")