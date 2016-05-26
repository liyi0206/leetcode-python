class Solution(object):
    def subsetsWithDup(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        self.nums=nums
        self.res=[sorted(nums),[]]
        for k in range(1,len(nums)):
            self.bt(0,nums,[],k)
        return self.res
    
    def bt(self,p,nums,tmp,k):
        if p == k:
            if sorted(tmp) not in self.res:
                self.res.append(sorted(tmp))
            return
        for i in range(len(nums)):
            self.bt(p+1,nums[i+1:],tmp+[nums[i]],k)
        
a=Solution()
print a.subsetsWithDup([1,2,2])