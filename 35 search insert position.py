class Solution(object):
    def searchInsert(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        #l, h = 0, len(nums) 
        #while l < h:
        #    m = (l + h) / 2
        #    if nums[m] < target:
        #        l = m + 1
        #    else:
        #        h = m
        #return l
        """
        1, at second last, nums[l],nums[m],nums[h] could only be -
        (1) a,a,a+1. target must be in [a,a+1], l=m+1 => nums[l]=nums[m]=nums[h]
        (2) b-1,b,b+1. if target>b, l=m+1 => nums[l]=nums[m]=nums[h]
                       if target<b, h=m-1 => nums[l]=nums[m]=nums[h]
        2, at last it must be nums[l]=nums[m]=nums[h]=c
        if target>c, l=m+1, yes
        if target<c, h=m-1, l=m yes
        """
        l, h = 0, len(nums)-1
        while l<=h:
            m=l+(h-l)/2
            if nums[m] == target: return m
            elif nums[m]>target: h=m-1
            else: l=m+1
        return l