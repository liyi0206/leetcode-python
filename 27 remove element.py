class Solution(object):
    def removeElement(self, nums, val): #naive, o(n^2)
        """
        :type nums: List[int]
        :type val: int
        :rtype: int
        """
        i=0
        while i<len(nums):
            if nums[i]==val: nums.remove(val)
            else: i+=1
        return len(nums)
        
    def removeElement2(self,nums,val): #two pointers, o(n)
        # similar to #26 remove dup
        p1,p2=0,0
        while p2<len(nums):
            if nums[p2]!=val:
                nums[p1]=nums[p2]
                p1+=1
            p2+=1
        return p1
        
a=Solution()
print a.removeElement([1,3,2,1,2],3) #4
print a.removeElement([3,3],3) #0