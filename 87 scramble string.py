class Solution(object):
    def isScramble(self, s1, s2):
        """
        :type s1: str
        :type s2: str
        :rtype: bool
        """
        if s1==s2: return True
        if len(s1)!=len(s2) or sorted(s1)!=sorted(s2): return False
        if len(s1)==1: return s1==s2
        for i in range(1,len(s1)):
            if self.isScramble(s1[:i],s2[:i]) and self.isScramble(s1[i:],s2[i:]):
                return True
            if self.isScramble(s1[:i],s2[-i:]) and self.isScramble(s1[i:],s2[:-i]):
                return True
        return False
        
a=Solution()
print a.isScramble("great","rgtae") #True
print a.isScramble("abcd","bdac") #False