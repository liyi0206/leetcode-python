class Solution(object):
    def jump(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        maxj, maxn, tms = 0, 0, 0
        for i in range(len(nums) - 1):
            maxn = max(maxn, nums[i] + i)
            if i == maxj:
                maxj, tms = maxn, tms + 1
        return tms