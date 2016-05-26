class Solution(object):
    def wiggleSort(self, nums): #nums[0] <= nums[1] >= nums[2] <= nums[3]...
        """
        :type nums: List[int]
        :rtype: void Do not return anything, modify nums in-place instead.
        """
        for i in range(1,len(nums)):
            if (i%2==1 and nums[i]<nums[i-1]) or (i%2==0 and nums[i]>nums[i-1]):
                nums[i],nums[i-1] = nums[i-1],nums[i]
            # swap would work, as at odd idx for example, nums[idx-2]>nums[idx-1]
            # if nums[idx] is smaller, it would still be smaller than nums[idx-2]

a=Solution()
nums=[3, 5, 2, 1, 6, 4]
a.wiggleSort(nums) 
print nums 