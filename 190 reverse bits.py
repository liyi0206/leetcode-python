class Solution(object):
    def reverseBits(self, n):
        """
        :type n: int
        :rtype: int
        """
        return int("".join(list(reversed(bin(n)[2:].zfill(32)))),2)
        
a=Solution()
print a.reverseBits(43261596)