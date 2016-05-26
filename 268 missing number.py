class Solution(object):
    def missingNumber(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        n = len(nums)+1
        xor = 0
        for i in range(n):
            xor ^= i
        xor2=0
        for num in nums:
            xor2 ^= num
        return xor^xor2
        
a=Solution()
print a.missingNumber([0, 1, 3])