class Solution(object):
    def removeDuplicates(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        #i=0
        #while i<len(nums)-2:
        #    if nums[i+2]==nums[i+1]==nums[i]:
        #        nums.remove(nums[i+2])
        #    else:
        #        i+=1
        #return len(nums)

        if len(nums)<=2: return len(nums)
        idx=2
        cnt=2 if nums[0]==nums[1] else 1
        for i in range(2,len(nums)):
            print i, nums[i]
            if nums[i]!=nums[idx-1] or cnt==1:
                cnt=2 if nums[i]==nums[idx-1] else 1
                nums[idx]=nums[i]
                idx+=1
            #print nums[:idx]
        return idx
        
a=Solution()
print a.removeDuplicates([1,1,1,2,2,3])
print a.removeDuplicates([1,1,1])