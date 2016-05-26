class Solution(object):
    def hammingWeight(self, n):
        """
        :type n: int
        :rtype: int
        """
        return sum(1 for c in bin(n) if c=="1")
        
a=Solution()
print a.hammingWeight(11)