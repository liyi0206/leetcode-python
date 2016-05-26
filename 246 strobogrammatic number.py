class Solution(object):
    def isStrobogrammatic(self, num):
        """
        :type num: str
        :rtype: bool
        """
        #if not num: return False
        #if len(num)==1: 
        #    if num in "18": return True
        #    else: return False
        mp={'6':'9','9':'6','8':'8','1':'1','0':'0'}
        n=len(num)
        for i in range(n/2+1):
            if num[i] not in mp or mp[num[i]]!=num[n-i-1]: return False
        return True
        
a=Solution()
print a.isStrobogrammatic('69')
print a.isStrobogrammatic('88')
print a.isStrobogrammatic('818')
print a.isStrobogrammatic('698')

print a.isStrobogrammatic('659')
print a.isStrobogrammatic('2')
print a.isStrobogrammatic('101')