class Solution(object):
    def isOneEditDistance(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: bool
        """
        ls,lt=len(s),len(t)
        if abs(ls-lt)>1: return False
        if abs(ls-lt)==1:
            for i in range(min(ls,lt)):
                if s[i]!=t[i]:
                    if (ls>lt and s[i+1:]==t[i:]) or (lt>ls and s[i:]==t[i+1:]):
                        return True
                    else: return False
            return True    
        if ls==lt:
            for i in range(ls):
                if s[i]!=t[i]:
                    if s[i+1:]==t[i+1:]: return True
                    else: return False
            return False
            
a=Solution()
print a.isOneEditDistance("cat","cts")
print a.isOneEditDistance("cat","cats")
print a.isOneEditDistance("dog","dig")
print a.isOneEditDistance("imac","mac")
print a.isOneEditDistance("","")
print a.isOneEditDistance("c","c")