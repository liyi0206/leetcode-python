class Solution(object):
    def minPatches(self, nums, n): # nums is sorted
        """
        :type nums: List[int]
        :type n: int
        :rtype: int
        """
        idx=0 # to iter through nums
        total=1 # [1,total) could be added by existing elems
        res=0
        while total<=n:
            # if there new number, 
            # only when the new num<=total, could we use it,
            # otherwise not all [1,total+num) could be added
            if idx<len(nums) and nums[idx]<=total:
                total+=nums[idx]
                idx+=1
            else:
                total<<=1 # we add 1,2,4,8,...
                res+=1
        return res
        
a=Solution()
print a.minPatches([1,3],6) #1
print a.minPatches([1,5,10],20) #2
print a.minPatches([1,2,2],5) #0

print a.minPatches([],16) #5 - [1,2,4,8,16]