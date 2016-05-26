class Solution(object):
    def singleNumber(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        res=0
        for a in nums:
            res ^= a
        return res
        
a=Solution()
print a.singleNumber([1,3,6,8,1,3,7,7,6])