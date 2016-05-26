class Solution(object):
    #def productExceptSelf(self, nums):
    #    """
    #    :type nums: List[int]
    #    :rtype: List[int]
    #    """
    #    prod,zeros=1,[]
    #    for i,n in enumerate(nums): 
    #        if n==0: zeros.append(i)
    #        else: prod*=n
    #    if len(zeros)>1: res=[0]*len(nums)
    #    elif len(zeros)==1: 
    #        idx=zeros[0]
    #        res=[0]*idx+[prod]+[0]*(len(nums)-idx-1)
    #    else:
    #        res=[]
    #        for n in nums: res.append(prod/n)
    #    return res
        
    def productExceptSelf(self,nums):
        size=len(nums)
        res=[1]*size
        left=1
        for x in range(size-1):
            left*=nums[x]
            res[x+1]*=left
        right=1
        for x in range(size-1,0,-1):
            right*=nums[x]
            res[x-1]*=right
        return res
        
a=Solution()
print a.productExceptSelf([1,2,3,4])
print a.productExceptSelf([1,2,0,4])
print a.productExceptSelf([1,0,0,4])