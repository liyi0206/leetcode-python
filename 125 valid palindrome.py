class Solution(object):
    def isPalindrome(self, s): #naive, o(n) time, o(n) space
        """
        :type s: str
        :rtype: bool
        """
        t=[l for l in s.lower() if l in "abcdefghijklmnopqrstuvwxyz0123456789"]
        for i in range(len(t)/2):
            if t[i]!=t[-i-1]: return False
        return True
        
    def isPalindrome2(self, s): #o(n) time, in place
        st=set("abcdefghijklmnopqrstuvwxyz0123456789")
        s=s.lower()
        p1,p2=0,len(s)-1
        while p1<p2:
            while s[p1] not in st and p1<p2: p1+=1
            while s[p2] not in st and p1<p2: p2-=1
            if s[p1]!=s[p2]: return False
            p1,p2=p1+1,p2-1
        return True
        
a=Solution()
print a.isPalindrome2("A man, a plan, a canal: Panama")
print a.isPalindrome2("race a car")
print a.isPalindrome2("")
print a.isPalindrome2("0P")
print a.isPalindrome2("aa")