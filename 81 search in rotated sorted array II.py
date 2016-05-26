class Solution(object):
    def search(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: bool
        """
        l,h = 0,len(nums)-1
        while (l<=h):
            m=l+(h-l)/2
            if nums[m] == target: return True
            if nums[m]==nums[l]==nums[h]: l,h = l+1,h-1 #new line
            elif (nums[l]<nums[m] and nums[l]<=target<nums[m]) or \
                 (nums[l]>nums[m] and not (nums[m]<target<=nums[h])):
                h=m-1
            else:
                l=m+1
        return False
        
    #def search1(self, nums, target):   
    #    l,h = 0,len(nums)-1
    #    while (l<=h):
    #        m=l+(h-l)/2
    #        if nums[m] == target: return True
    #        elif (nums[l]<nums[m] and nums[l]<=target<nums[m]) or \
    #             (nums[l]>nums[m] and not (nums[m]<target<=nums[h])):
    #            h=m-1
    #        else:
    #            l=m+1
    #    return False
        
a=Solution()
print a.search([1,3,1,1,1],3)
#print a.search1([1,3,1,1,1],3) #wrong
#print a.search1([1,3,0,1,1],3) #right
#print a.search1([2,3,1,1,1],3) #right
#print a.search1([1,1,1,3,0],3) #right
# not possible to have input [1,3,1,x,x] with x>1 or x<1.