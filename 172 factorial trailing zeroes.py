class Solution(object):
    def trailingZeroes(self, n):
        """
        :type n: int
        :rtype: int
        """
        if n==0: return 0
        import math
        m=int(math.log(n,5))
        res=0
        for i in range(1,m+1):
            res+=n/(5**i)
        return res