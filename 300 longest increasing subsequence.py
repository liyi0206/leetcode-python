class Solution(object):
    def lengthOfLIS(self, nums): #o(n^2)
        """
        :type nums: List[int]
        :rtype: int
        """
        if not nums: return 0
        dp = [1]*len(nums)
        for x in range(len(nums)):
            for y in range(x):
                if nums[x] > nums[y]: 
                    dp[x] = max(dp[x], dp[y]+1)
            #print dp
        return max(dp)
        
    def lengthOfLIS2(self, nums): #o(nlogn)
        size = len(nums)
        dp = []
        for x in range(size):
            l,h = 0,len(dp)-1
            while l<= h:
                m=(l+h)/2
                if dp[m]>=nums[x]: h=m-1
                else: l=m+1
            if l>=len(dp): dp.append(nums[x])
            else: dp[l] = nums[x]
        return len(dp)
        
        
a=Solution()
print a.lengthOfLIS2([10,9,2,5,3,7,101,18]) #4 from [2,3,7,101]