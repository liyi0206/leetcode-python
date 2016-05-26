class Solution(object):
    def nextPermutation(self, nums): #o(n), while doing all permutations is o(n!)
        """
        :type nums: List[int]
        :rtype: void Do not return anything, modify nums in-place instead.
        """
        # find the rightmost pair k,k+1 that nums[k]<nums[k+1]
        # (everything after it is descending)
        # find rightmost l that nums[l]>nums[k], swap l,k to secure the idx
        # reverse the descending numbers after k, to make it ascending
        # (must be ascending, because nums[l]>nums[k]>nums[l+1])
        
        k,l = -1,0
        for i in range(len(nums)-1):
            if nums[i]<nums[i+1]: k=i
        # if no such i, reverse nums to start over
        if k==-1: nums.reverse()
        else:
            for i in range(len(nums)):
                if nums[i]>nums[k]: l=i
            nums[k],nums[l]=nums[l],nums[k]
            # reverse the descending sequence
            nums[k+1:]=nums[:k:-1]
