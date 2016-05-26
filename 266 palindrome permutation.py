class Solution(object):
    def canPermutePalindrome(self, s):
        """
        :type s: str
        :rtype: bool
        """
        mp={}
        for c in s:
            if c not in mp: mp[c]=1
            else: mp[c]+=1
        odd=0
        for k in mp:
            if mp[k]%2==1: odd+=1
            if odd==2: return False
        return True
        
a=Solution()
print a.canPermutePalindrome("code") #F
print a.canPermutePalindrome("aab") #T
print a.canPermutePalindrome("carerac") #T