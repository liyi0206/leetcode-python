class Solution(object):
    def rob(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        if len(nums) == 1: return nums[0]
        # add one more restriction, might need to rob one less house
        return max(self.robLinear(nums[1:]), self.robLinear(nums[:-1]))
        
    def robLinear(self,nums):
        pp,p,cur=0,0,0
        for i in range(len(nums)):
            cur=max(p,pp+nums[i])
            pp,p=p,cur
        return cur