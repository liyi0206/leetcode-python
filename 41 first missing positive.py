class Solution(object):
    def firstMissingPositive(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        i=0
        #print nums
        while i<len(nums):
            if nums[i]-1<len(nums) and nums[i]-1>=0 and nums[i]!=nums[nums[i]-1]:
                #print "swap",nums[i],nums[nums[i]-1]
                nums[nums[i]-1],nums[i] = nums[i],nums[nums[i]-1]
                #print nums
            else: i+=1
        print nums
        for i in range(len(nums)):
            if nums[i]!=i+1:
                return i+1
        return len(nums)+1
                
a=Solution()
print a.firstMissingPositive([1,2,0]) #3
print a.firstMissingPositive([3,4,-1,1]) #2
print a.firstMissingPositive([2]) #1