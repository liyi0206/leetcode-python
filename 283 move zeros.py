class Solution(object):
    def moveZeroes(self, nums): #naive, o(n^2)
        """
        :type nums: List[int]
        :rtype: void Do not return anything, modify nums in-place instead.
        """
        cnt = sum([1 for num in nums if num==0])
        for i in range(cnt):
            nums.remove(0)
            nums.append(0)
            
    def moveZeroes2(self, nums): #two pointers, o(n)
        p1,p2=0,0
        while p2<len(nums):
            if nums[p2]!=0: 
                nums[p1],nums[p2]=nums[p2],nums[p1]#
                p1,p2=p1+1,p2+1
            else:
                while p2<len(nums)-1 and nums[p2]==0: p2+=1
                nums[p1],nums[p2]=nums[p2],nums[p1]
                p1,p2=p1+1,p2+1
                
    def moveZeroes3(self, nums): #simplify two pointers, o(n)
        p1,p2=0,0
        while p2<len(nums):
            if nums[p2]==0: 
                while p2<len(nums)-1 and nums[p2]==0: p2+=1
            nums[p1],nums[p2]=nums[p2],nums[p1]#
            p1,p2=p1+1,p2+1

a=Solution()
nums=[0, 1, 0, 3, 12]
a.moveZeroes2(nums)
print nums