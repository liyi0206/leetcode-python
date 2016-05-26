class Solution(object):
    def combine(self, n, k):
        """
        :type n: int
        :type k: int
        :rtype: List[List[int]]
        """
        self.nums,self.k=range(1,n+1),k
        self.res=[]
        self.bt(0,range(1,n+1),[])
        return self.res
        
    def bt(self,p,nums,tmp):
        if p == self.k:
            self.res.append(tmp)
            return
        for i in range(len(nums)):
            self.bt(p+1,nums[i+1:],tmp+[nums[i]])

a=Solution()
print a.combine(4,2)