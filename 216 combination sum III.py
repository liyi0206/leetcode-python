class Solution(object):
    def combinationSum3(self, k, n):
        """
        :type k: int
        :type n: int
        :rtype: List[List[int]]
        """
        self.t,self.c = n,range(1,10)
        self.res=[]
        self.bt(k,0,[])
        return self.res
        
    def bt(self,k,p,tmp):
        if k==0:
            if sum(tmp) == self.t:
                self.res.append(tmp)
            return
        for i in range(p,len(self.c)):
            self.bt(k-1,i+1,tmp+[self.c[i]])
            
a=Solution()
print a.combinationSum3(3,9)