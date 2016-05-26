class Solution(object):
    def canJump(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        if nums==[]: return False
        maxJump=nums[0]
        for i in range(1,len(nums)):
            maxJump-=1
            if (maxJump<0):
                return False
            maxJump=max(maxJump, nums[i])
        return True