class Solution(object):
    def titleToNumber(self, s):
        """
        :type s: str
        :rtype: int
        """
        mp={}
        for i in range(26):
            mp[chr(ord('A')+i)]=i+1
        #print mp
        res=0
        for c in s:
            res=res*26+mp[c]
        return res

a=Solution()
print a.titleToNumber('AB') #28
print a.titleToNumber('Z') #26
print a.titleToNumber('AAZ') #52