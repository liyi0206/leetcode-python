class Solution(object):
    def findMin(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        #l,h=0,len(nums)-1
        #while l<=h:
        #    m=(l+h)/2
        #    if nums[m]<nums[l]:h=m
        #    elif nums[l]>nums[h]: l=m+1
        #    else: h=m-1
        #return nums[l]
        
        l,h=0,len(nums)-1
        while nums[l]>nums[h]:
            m=(l+h)/2
            if nums[m]>nums[h]: l=m+1
            else: h=m
        return nums[l]
        
a=Solution()
print a.findMin([4,5,6,7,0,1,2,3]) #0
print a.findMin([2,1]) #1
print a.findMin([3,1,2]) #1