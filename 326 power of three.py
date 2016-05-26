class Solution(object):
    def isPowerOfThree(self, n): #best
        """
        :type n: int
        :rtype: bool
        """
        # 1162261467 is 3^19,  3^20 is bigger than int
        # 3^19 < (2<<30), 3^20 < (2<<30)
        return n>0 and 1162261467%n==0
        
    def isPowerOfThreeIter(self,n):
        while n>1:
            if n%3>0: return False
            n=n/3
        return n==1 # avoid n==0 case
        
a=Solution()
print a.isPowerOfThree(9)