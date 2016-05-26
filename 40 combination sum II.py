class Solution:
    # @param candidates, a list of integers
    # @param target, integer
    # @return a list of lists of integers
    def combinationSum(self, candidates, target):
        #candidates=list(set(candidates))
        self.t,self.c = target, sorted(candidates)
        self.res=[]
        self.bt(0,[])
        return self.res
        
    def bt(self,p,tmp):
        if sum(tmp)==self.t:
            if tmp not in self.res:
                self.res.append(tmp)
            return
        for i in range(p,len(self.c)):
            if sum(tmp+[self.c[i]])<=self.t:
                self.bt(i+1,tmp+[self.c[i]])