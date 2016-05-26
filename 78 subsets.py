class Solution(object):
    def subsets(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        self.nums,self.n=sorted(nums),len(nums)
        self.res=[[]]
        for i in range(self.n):
            self.bt(i,[self.nums[i]])
        return self.res
        
    def bt(self,i,tmp):
        self.res.append(tmp)
        for j in range(i+1,self.n):
            self.bt(j,tmp+[self.nums[j]])
 
class Solution2(object): # same as sol1, just less loop
    def subsets(self,nums):
        nums.sort()
        self.res=[]
        self.dfs([],nums)
        return self.res
         
    def dfs(self,tmp,nums): #subset numbers, residual numbers
        self.res.append(tmp)
        for i in range(len(nums)):
            self.dfs(tmp+[nums[i]],nums[i+1:])
               
class Solution3(object): # ready for generalized abbreviation
    def subsets(self, nums):
        self.nums=sorted(nums)
        self.res=[]
        self.dfs([],0)
        return self.res

    def dfs(self,cur,n):
        if n==len(self.nums): 
            self.res.append(cur)
            return
        # for every element, use it or not
        self.dfs(cur,n+1)
        self.dfs(cur+[self.nums[n]],n+1)

class Solution4(object): # iterative       
    def subsets(self, nums):
        nums.sort()
        res = [[]]
        for x in nums:
            for i in range(len(res)):
                res.append(res[i]+[x])
        return res

a=Solution()
print a.subsets([1,2,3])