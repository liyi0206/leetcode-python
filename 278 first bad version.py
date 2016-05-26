# The isBadVersion API is already defined for you.
# @param version, an integer
# @return a bool
#def isBadVersion(version):

class Solution(object):
    def firstBadVersion(self, n):
        """
        :type n: int
        :rtype: int
        """
        if n==1: return 1 if isBadVersion(n) else 0
        l,h=1,n
        while l<h:
            m=l+(h-l)/2
            if isBadVersion(m): h=m
            else: l=m+1
        return l
 
def isBadVersion(version):
    if version>3: return True
    else: return False           
a=Solution()
print a.firstBadVersion(10) #4

#def isBadVersion(version):
#    return True           
#a=Solution()
#print a.firstBadVersion(1) #1