class Solution(object):
    def largestNumber(self, nums):
        """
        :type nums: List[int]
        :rtype: str
        """
        nums = sorted([str(x) for x in nums], cmp = self.compare)
        res = ''.join(nums).lstrip('0')
        return res or '0'

    def compare(self, a, b):
        return [1, -1][a+b > b+a]
        
a=Solution()
print a.largestNumber([3, 30, 34, 5, 9]) 