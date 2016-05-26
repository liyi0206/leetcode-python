class Solution(object):
    #def isPowerOfTwo(self, n):
    #    """
    #    :type n: int
    #    :rtype: bool
    #    """
    #    if n<=0: return False
    #    while n>1:
    #        m =n%2
    #        if m==1:  return False
    #        else: n /= 2
    #    return True
        
    def isPowerOfTwo(self, n):
        return n>0 and n&(n-1) == 0
        
a=Solution()
print a.isPowerOfTwo(6)