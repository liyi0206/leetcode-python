class Solution(object):
    def strobogrammaticInRange(self, low, high):
        """
        :type low: str
        :type high: str
        :rtype: int
        """
        self.low,self.high=int(low),int(high)
        lens=range(len(low),len(high)+1)
        symmetrics='018'
        self.mp={'6':'9','9':'6','8':'8','1':'1','0':'0'}
        self.res=0
        for n in lens:
            if n%2==1: 
                for c in symmetrics: self.recur(n/2,c)
            else: 
                self.recur(n/2,'')
        return self.res
            
    def recur(self,i,tmp):
        if i==0: 
            if (len(tmp)==1 or tmp[0]!='0') and self.low<=int(tmp)<=self.high:
                self.res+=1
            return
        for k in self.mp:
            self.recur(i-1,k+tmp+self.mp[k])
            
a=Solution()
print a.strobogrammaticInRange('50','100')