class Solution(object): # o(n) memoery, not optimal
    def rob(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        if not nums: return 0
        size = len(nums)
        dp = [nums[0]]+[max(nums[0:2])]+[0]*(size-2)
        for i in range(2, size):
            dp[i] = max(dp[i-1], dp[i-2]+nums[i])
        return dp[-1]
        
    def rob2(self,nums): # most concise
        pp,p,cur=0,0,0
        for i in range(len(nums)):
            cur=max(p,pp+nums[i])
            pp,p=p,cur
        return cur
                
    def rob3(self,nums): # similar to codes of 276 paint fence
        if not nums: return 0
        if len(nums)<3: return max(nums)
        pp,p=nums[0],max(nums[0:2])
        cur=0
        for i in range(2,len(nums)):
            cur=max(p,pp+nums[i])
            pp,p=p,cur
        return cur