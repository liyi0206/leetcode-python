class Solution(object): #naive
    def countSmaller1(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        res=[]
        for i in range(len(nums)-1):
            res.append(len([1 for a in nums[i+1:] if a<nums[i]]))
        res.append(0)
        return res
  
class Solution1(object): # BST
    def countSmaller(self, nums):
        tmp=[] #contains elem from last backward, should be bst=BST()
        res=[]
        for i in range(len(nums)-1,-1,-1):
            print tmp,nums[i],
            idx=self.binarySearch(tmp,nums[i])
            res.insert(0,idx)
            tmp.insert(idx,nums[i])  #need to use BST, o/w insert is o(n)
        return res
        
    def binarySearch(self,nums,target):
        if not nums: return 0
        l,h = 0,len(nums)-1
        while l<=h:
            m=l+(h-l)/2
            if nums[m]==target: 
                while m>=0 and nums[m] == target: m-=1 
                return m+1
            elif nums[m]>target:h=m-1
            else: l=m+1
        return l
        
a=Solution()
print a.countSmaller([5, 2, 6, 1]) #[2, 1, 1, 0]
print a.countSmaller([-1,-1])