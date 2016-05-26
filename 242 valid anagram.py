class Solution(object):
    def isAnagram(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: bool
        """
        mp1,mp2={},{}
        for c in s:
            if c not in mp1: mp1[c]=1
            else: mp1[c]+=1
        for c in t:
            if c not in mp2: mp2[c]=1
            else: mp2[c]+=1
        return mp1==mp2
        
a=Solution()
print a.isAnagram(s = "anagram", t = "nagaram")
print a.isAnagram(s = "rat", t = "car")