class Solution(object):
    def singleNumber(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        K = 32 # assuming 32 bit integers
        R = 3 # repeat for 3 times
        res = 0
        
        bit = 1
        for k in range(K):
            ct = sum([1 for n in nums if abs(n)&bit])
            if ct%R: res += bit
            bit <<= 1
        ct = sum([1 for x in nums if x==res])
        return res if ct%R in range(1,R) else -res
        
a=Solution()
print a.singleNumber([1,2,3,1,1,2,3,1,2,3])
print a.singleNumber([1,2,3,1,1,2,3,1,2,3,1])
print a.singleNumber([-1,2,3,-1,-1,2,3,-1,2,3])
print a.singleNumber([-1,2,3,1,1,2,3,1,2,3])