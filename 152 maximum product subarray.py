class Solution(object):
    def maxProduct(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        res = nums[0]
        minp,maxp = nums[0],nums[0]
        for a in nums[1:]:
            tmp_maxp = maxp
            tmp_minp = minp
            maxp = max(tmp_maxp*a, tmp_minp*a, a)
            minp = min(tmp_maxp*a, tmp_minp*a, a)
            res = max(res, maxp)
        return res
        
        
a=Solution()
#print a.maxProduct([2,3,-2,4]) #6 from [2,3]
print a.maxProduct([2,3,-2,4,5])
print a.maxProduct([-2,0,-1])