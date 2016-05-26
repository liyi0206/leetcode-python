class Solution(object):
    #def permute(self, nums):
    #    """
    #    :type nums: List[int]
    #    :rtype: List[List[int]]
    #    """
    #    self.res=[]
    #    self.bt(nums, [])
    #    return self.res
    #        
    #def bt(self, nums, tmp):
    #    if len(nums) == 0:
    #        self.res.append(tmp)
    #        return
    #    for i in range(len(tmp)+1):
    #        self.bt(nums[1:], tmp[:i]+[nums[0]]+tmp[i:])
    
    def permute(self, nums):
        self.res=[]
        self.bt(nums,[]) #void
        return self.res
        
    def bt(self,nums,tmp):
        if len(nums) == 0:
            self.res.append(tmp) #don't need return, as range(-1,-1,-1) is [], do nothing
        for i in range(len(nums)-1,-1,-1):
            self.bt(nums[:i]+nums[i+1:],tmp+[nums[i]])
               
a=Solution()
print a.permute([1,2,3])