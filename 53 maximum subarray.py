# -*- coding: utf-8 -*-
class Solution(object):
    def maxSubArray(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        res, sum = nums[0], nums[0]
        for num in nums[1:]:
            sum = num if sum<=0 else sum+num
            res = max(res, sum)
        return res
   
a=Solution()
print a.maxSubArray([-2,1,-3,4,-1,2,1,-5,4])