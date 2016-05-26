class Solution(object):
    def search(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        l,h = 0,len(nums)-1
        while (l<=h):
            m=l+(h-l)/2
            if nums[m] == target: return m
            elif (nums[l]<nums[m] and nums[l]<=target<nums[m]) or \
                 (nums[l]>nums[m] and not (nums[m]<target<=nums[h])):
                h=m-1
            else:
                l=m+1
        return -1