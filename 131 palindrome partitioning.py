class Solution(object):
    def partition(self, s):
        """
        :type s: str
        :rtype: List[List[str]]
        """
        self.res=[]
        self.bt(s,[])
        return self.res
        
    def bt(self,s,tmp):
        if len(s)==0: self.res.append(tmp)
        else:
            for i in range(1,len(s)+1):
                if self.is_valid(s[:i]):
                    self.bt(s[i:],tmp+[s[:i]])
                
    def is_valid(self,s): #assuming len(s)>0
        if len(s)==1: return True
        for i in range(len(s)/2):
            if s[i]!=s[len(s)-i-1]: 
                return False
        return True
        
a=Solution()
print a.partition("aab")
print a.partition("bb")