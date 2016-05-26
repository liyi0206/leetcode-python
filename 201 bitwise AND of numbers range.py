class Solution(object):
    def rangeBitwiseAnd(self, m, n):
        """
        :type m: int
        :type n: int
        :rtype: int
        """
        #res=m
        #for i in range(m+1,n+1):
        #    res &= i
        #return res
        bit = 0
        while m!=n:
            m >>= 1
            n >>= 1
            bit +=1
        return m<<bit
        
        
a=Solution()
print a.rangeBitwiseAnd(5,7)
print a.rangeBitwiseAnd(8,25)