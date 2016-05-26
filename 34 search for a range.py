class Solution(object):
    def searchRange(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        res=[-1,-1]
        if nums[0] > target or nums[-1] < target: return res
        l,h=0,len(nums)-1
        while l <= h:
            m=l+(h-l)/2
            if nums[m] == target:
                h,l=m,m
                while l >= 0 and nums[l]==target: l-=1
                res[0]=l+1
                while h < len(nums) and nums[h]==target: h+=1
                res[1]=h-1
                return res
            elif nums[m] > target: h=m-1
            else: l=m+1
        return res
        
#    def searchRange(self, nums, target):
#        return [self.lower_bound(nums, target), self.upper_bound(nums, target)]
#
#    def lower_bound(self, A, target):
#        l,h= 0,len(A)
#        while l < h:
#            m = (l+h)/2
#            if A[m] < target: l = m+1
#            else: h = m
#        return l if l < len(A) and A[l] == target else -1
#
#    def upper_bound(self, A, target):
#        l,h = 0,len(A)-1
#        while l < h:
#            m = (l+h)/2
#            if A[m] <= target: l = m+1
#            else: h = m-1
#        return l-1 if l-1 < len(A) and A[l-1] == target else -1
    
# edge case: [1], 1
    
"""
Given nums= [5,7,7,8,8,10], target= 8
      index=[0,1,2,3,4,5] ->correct ans=[3,4]
h=len(nums), l<h, l,l-1
lower: 0,2,5->3,4,5->3,3,3
upper: 0,2,5->3,4,5->5,5,5

h=len(nums)-1,l<h,l,l
lower: 0,2,4->3,3,4->3,3,3 return 3
upper: 0,2,4->3,3,4->4,4,4 return 4
"""