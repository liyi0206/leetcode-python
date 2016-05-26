class Solution(object):
    def numTrees(self, n):
        """
        :type n: int
        :rtype: int
        """
        if n<=0: return 0
        res=[1,1]+[0]*(n-1)
        for i in range(2,n+1):
            for j in range(i):
                res[i]+=res[j]*res[i-j-1]
        return res[-1]
        
a=Solution()
print a.numTrees(3)