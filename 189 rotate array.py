class Solution(object):
    def rotate(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: void Do not return anything, modify nums in-place instead.
        """
        k=k%len(nums)
        n,l=len(nums),len(nums)-k
        for i in range(l/2):
            nums[i],nums[l-i-1] = nums[l-i-1],nums[i]
        for j in range(k/2):
            nums[l+j],nums[n-j-1] = nums[n-j-1],nums[l+j]
        for k in range(n/2):
            nums[k],nums[n-k-1] = nums[n-k-1],nums[k]
        
        
a=Solution()
nums = [1,2,3,4,5,6,7]
a.rotate(nums,3)
print nums #[5,6,7,1,2,3,4]