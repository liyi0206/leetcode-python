class Solution(object):
    def sortColors(self, nums):
        """
        :type nums: List[int]
        :rtype: void Do not return anything, modify nums in-place instead.
        """
        p1,p2 = 0,len(nums)-1
        i=0
        while i<=p2:
            if nums[i]==0:
                nums[i],nums[p1]=nums[p1],nums[i]
                p1+=1
                i+=1
            elif nums[i]==1: i+=1
            else: 
                nums[i],nums[p2]=nums[p2],nums[i]
                p2-=1
        
        
a=Solution()
nums=[0,1,2,0,2,1]
a.sortColors(nums)
print nums