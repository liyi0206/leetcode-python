# -*- coding: utf-8 -*-
class Solution(object):
    # given num[-1] = num[n] = -inf, worst case would be an ascending array.
    # if we iterate one by one
        
    def findPeakElement(self, nums): # o(n) time, 2n compare 
        """
        :type nums: List[int]
        :rtype: int
        """
        if not nums: return None
        if len(nums)==1: return 0
        if nums[0]>nums[1]: return 0
        if nums[-1]>nums[-2]: return len(nums)-1
        for i in range(1,len(nums)-1):
            if nums[i]>nums[i-1] and nums[i]>nums[i+1]:
                return i
        
    def findPeakElement2(self, nums): # o(n) time, n compare 
        if not nums: return None
        if len(nums)==1: return 0
        if nums[-1]>nums[-2]: return len(nums)-1
        for i in range(1,len(nums)):
            if nums[i-1]>nums[i]:
                return i-1
        
    def findPeakElement3(self, nums): #o(logn) time ****
        # in usual case will do o(logn), no early returns
        
        l,h = 0,len(nums)-1
        while l<=h:
            # number at l is larger than left
            # number at h is larger than right
            if l==h: return l
            m=(l+h)/2
                    # might waste peaks in the first half, but doesn't matter
                    # as in worst case, last idx is the peak
                    # as long as find a number smaller than left
            if nums[m]<nums[m+1]: l=m+1 # given num[i]!=num[i+1]
                    # might waste, but doesn't matter.
                    # as long as find a number smaller than right
            else: h=m
        
a=Solution()
print a.findPeakElement([1, 2, 3, 1])