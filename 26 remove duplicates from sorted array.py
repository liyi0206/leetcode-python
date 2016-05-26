class Solution(object):
    def removeDuplicates(self, nums): #naive, o(n^2)
        """
        :type nums: List[int]
        :rtype: int
        """
        i=0
        while i<len(nums)-1:
            if nums[i+1]==nums[i]: nums.remove(nums[i+1])
            else: i+=1
        return len(nums)
        
    def removeDuplicates2(self, nums): #two pointers, o(n), best
        if not nums: return 0
        p1,p2=1,1
        while p2<len(nums):
            if nums[p2]!=nums[p2-1]:
                nums[p1]=nums[p2]
                p1+=1
            p2+=1
        return p1
        
    def removeDuplicates3(self, nums): #two pointers, o(n), mine
        # 1, returning new length makes it much harder, 
        # otherwise the same as remove zeroes
        # 2, just override, don't swap, otherwise new dup will be hard to find
        if not nums: return 0
        p1,p2=1,1
        while p2<len(nums):
            if nums[p2]==nums[p2-1]:
                while p2<len(nums)-1 and nums[p2]==nums[p2-1]: p2+=1
            if nums[p2]!=nums[p2-1]:
                nums[p1]=nums[p2]
                p1,p2=p1+1,p2+1
            else: break
        return p1
            
a=Solution()
print a.removeDuplicates3([1,1,2]) #2
print a.removeDuplicates3([1,1]) #1
nums=[1,1,2,2]
print a.removeDuplicates3(nums) #2
print nums
