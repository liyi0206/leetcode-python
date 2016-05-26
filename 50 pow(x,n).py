class Solution(object):
    def myPow(self, x, n): # easiest to understand
        """
        :type x: float
        :type n: int
        :rtype: float
        """
        if n==0:return 1
        if n<0: return 1.0/self.myPow(x,-n)
        half= self.myPow(x, n/2)
        res = half*half
        if n&1: res*=x
        return res
        
class Solution1: # Recursion from stefan
    def myPow(self, x, n):
        if not n: return 1
        if n<0: return 1/self.myPow(x,-n) #why could pass without using 1.0?
        if n%2: return x*self.myPow(x,n-1)
        return self.myPow(x*x, n/2)
        
class Solution2: # Iteration from stefan
    def myPow(self, x, n):
        if n<0:
            x=1/x
            n=-n
        res=1
        while n:
            if n&1: res*=x
            x*=x
            n>>=1
        return res