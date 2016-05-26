class Solution(object):
    def findMin(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        l,h=0,len(nums)-1
        while l<h and nums[l]>=nums[h]:
            m=(l+h)/2
            if nums[m]>nums[h]: l=m+1
            elif nums[m]<nums[l]: h=m
            else: l=l+1 #n(l)==n(m)==n(h) #don't move h b/c h might be min
        return nums[l]
        
a=Solution()
print a.findMin([4,5,6,6,7,0,1,2,2,3]) #0
print a.findMin([3,3,1,3])#1
print a.findMin([10,1,10,10,10])#1

print a.findMin([2,1]) #1
print a.findMin([3,1,2]) #1

print a.findMin([1,2,2,2,0,1,1])#0
print a.findMin([1,2,1])#1
print a.findMin([0,1,1,0])#0