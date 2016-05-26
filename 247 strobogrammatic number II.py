class Solution(object):
    def findStrobogrammatic(self, n):
        """
        :type n: int
        :rtype: List[str]
        """
        if n==0: return []
        symmetrics='018'
        self.mp={'6':'9','9':'6','8':'8','1':'1','0':'0'}
        self.res=[]
        if n%2==1: 
            for c in symmetrics: self.recur(n/2,c)
        else: 
            self.recur(n/2,'')
        return self.res
            
    def recur(self,i,tmp):
        #print i,tmp
        if i==0: 
            if len(tmp)==1 or tmp[0]!='0':
                self.res.append(tmp)
            return
        for k in self.mp:
            self.recur(i-1,k+tmp+self.mp[k])
            
a=Solution()
print a.findStrobogrammatic(0)
print a.findStrobogrammatic(1)
print a.findStrobogrammatic(2)
print a.findStrobogrammatic(3)