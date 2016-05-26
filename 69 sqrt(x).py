class Solution(object):
    def mySqrt(self, x):
        """
        :type x: int
        :rtype: int
        """
        l,h=0,x # not x-1, as edge case x=1
        while l<=h:
            m=l+(h-l)/2
            tmp=m*m
            if tmp==x: return m
            elif tmp<x: l=m+1
            else: h=m-1
        return h # not l, as need the floor
        
a=Solution()
print a.mySqrt(8)