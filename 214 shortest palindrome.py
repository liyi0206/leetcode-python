class Solution(object):
    def shortestPalindrome(self, s): # TLE
        """
        :type s: str
        :rtype: str
        """
        self.s,self.l=s,len(s)
        for i in range(self.l/2,-1,-1):
            print i
            if self.check2(i): #k is left center
                return ''.join(list(reversed(s[i*2+2:])))+s
            if self.check1(i): #k is center
                return ''.join(list(reversed(s[i*2+1:])))+s
            
    def check1(self,k):
        l,r=k-1,k+1
        while l>=0 and r<self.l:
            if self.s[l]!=self.s[r]: return False
            l,r=l-1,r+1
        return True
        
    def check2(self,k):
        if self.l%2==1 and k==self.l/2: return False
        l,r=k,k+1
        while l>=0 and r<self.l:
            if self.s[l]!=self.s[r]: return False
            l,r=l-1,r+1
        return True

class Solution2(object): #robin karp, AC
    def shortestPalindrome(self, s): # full version
        rev_s = s[::-1]
        N = len(s)
        K = 26
        Q = 104729 #any large prime number
         
        hs,hsr = 0,0
        maxLen = 0 
        Kn = 1
        for n in range(N):
            # starting point fixed, only extend, not shift
            hs = (hs*K+self.lk(s[n]))%Q  # s[:n+1]
            hsr= (hsr+Kn*self.lk(rev_s[N-n-1]))%Q  # rev_s[N-n-1:]
            # find the longest palindrome substring in self
            # the latter part is to ensure no hash collision
            if hs==hsr and s[:n+1]==rev_s[N-1-n:]: 
                maxLen = max(maxLen,n+1)
            Kn*=K
        return rev_s[:N-maxLen]+s
        
    def shortestPalindrome2(self, s): #simplified version, regardless of overflow and collision
        rev_s = s[::-1]
        N = len(s)
        K = 26
        hs,hsr = 0,0
        maxLen = 0 
        Kn = 1
        for n in range(N):
            # starting point fixed, only extend, not shift
            hs = (hs*K+self.lk(s[n]))  # s[:n+1]
            hsr= (hsr+Kn*self.lk(rev_s[N-n-1]))  # rev_s[N-n-1:]
            # find the longest palindrome substring in self
            # the latter part is to ensure no hash collision
            if hs==hsr: maxLen = max(maxLen,n+1)
            Kn*=K
        return rev_s[:N-maxLen]+s
 
    def lk(self,x):
        return ord(x)-ord('a')
 
class Solution3(object):
    def shortestPalindrome(self, s): #KMP, AC. which I don't understand
        """
        :type s: str
        :rtype: str
        """
        rev_s = s[::-1]
        l = s+'#'+rev_s
        p = [0]*len(l)
        for i in range(1,len(l)):
          j = p[i-1]
          while j>0 and l[i]!=l[j]:
            j = p[j-1]
          p[i] = j+(l[i]==l[j])
        return rev_s[:len(s)-p[-1]]+s
                   
a=Solution()
print a.shortestPalindrome("aacecaaa") #"aaacecaaa"
print a.shortestPalindrome("abcd") #"dcbabcd"