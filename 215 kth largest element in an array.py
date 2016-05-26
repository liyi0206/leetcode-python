import random
class Solution(object):
    def findKthLargest(self, nums, k): #quick select o(n), worst case o(nlogn)
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """
        pivot = random.choice(nums) #pivot is a number, not an idx
        nums1,nums2 = [],[]
        for num in nums:
            if num>pivot: nums1.append(num)
            elif num<pivot: nums2.append(num)
        if k<= len(nums1): 
            return self.findKthLargest(nums1, k)
        if k>len(nums)-len(nums2):
            return self.findKthLargest(nums2, k-(len(nums)-len(nums2)))
        return pivot #when k is the kth largest number
        
a=Solution()
print a.findKthLargest([3,2,1,5,6,4],2)