class Solution(object):
    def combinationSum(self, candidates, target):
        """
        :type candidates: List[int]
        :type target: int
        :rtype: List[List[int]]
        """
        # candidate could be a global static variable, as repeated number 
        # may be chosen unlimited number of times
        self.t,self.c = target, sorted(candidates)
        self.res=[]
        self.bt(0,[])
        return self.res
        
    def bt(self,p,tmp):
        if sum(tmp)==self.t:
            self.res.append(tmp)
            return
        for i in range(p,len(self.c)):
            if sum(tmp+[self.c[i]])<=self.t:
                self.bt(i,tmp+[self.c[i]])
            
a=Solution()
print a.combinationSum([2,3,6,7],7)
#print a.combinationSum([34,24,39,49,35,41,48,40,26,32,43,29,45,31,46,20,42,33,22,23,27,25,28,47,21,38,37,30,44],66)
#print a.combinationSum([47,36,30,38,22,41,45,35,32,28,46,48,40,24,39,23,42,21,33,43,31,26,27,37,29,34,49,20],61)
#print a.combinationSum([92,71,89,74,102,91,70,119,86,116,114,106,80,81,115,99,117,93,76,77,111,110,75,104,95,112,94,73],310)