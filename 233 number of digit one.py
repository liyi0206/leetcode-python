class Solution(object):
    def countDigitOne(self, n):
        """
        :type n: int
        :rtype: int
        """
        num_digits=len(str(n))
        res=0
        for i in range(num_digits):
            unit=10**i
            res+=unit*(n/unit/10)+max(min(n%(unit*10)-unit,unit-1)+1,0)
            
        return res
        
a=Solution()
print a.countDigitOne(13)
print a.countDigitOne(123)