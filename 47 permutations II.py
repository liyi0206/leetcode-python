class Solution(object):
    def permute(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        solutions = [[]]
        for num in nums:
            next = []
            for solution in solutions:
                for i in range(len(solution) + 1):
                    candidate = solution[:i] + [num] + solution[i:]
                    if candidate not in next:
                        next.append(candidate)
            solutions = next
        return solutions
    
    # Time Limit Exceeded [1,1,0,0,1,-1,-1,1]
    #def permute(self, nums):
    #    self.res=[]
    #    self.bt(nums,[]) #void
    #    return self.res
    #    
    #def bt(self,nums,tmp):
    #    if len(nums) == 0:
    #        if tmp not in self.res:
    #            self.res.append(tmp) 
    #    for i in range(len(nums)-1,-1,-1):
    #        self.bt(nums[:i]+nums[i+1:],tmp+[nums[i]])
            
a=Solution()
print a.permute([1,1,2])
print a.permute([1,1,0,0,1,-1,-1,1])