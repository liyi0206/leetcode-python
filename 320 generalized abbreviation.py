class Solution(object):
    def generateAbbreviations(self, word):
        """
        :type word: str
        :rtype: List[str]
        """
        self.word,self.n = word,len(word)   
        self.res = []
        self.bt('',0,0)
        return self.res
        
    def bt(self,cur,i,count): # current string, cnt of used digits, cnt of mask
        if i==self.n: # at last, only append count
            self.res.append(cur+str(count) if count>0 else cur)
            return     
        self.bt(cur,i+1,count+1)
        self.bt(cur+(str(count) if count>0 else '')+self.word[i],i+1,0) 
        # there is count i before word[i] (which is the i+1 th)
        # once used the count, push a char, and reset count to 0
        
a=Solution()
print a.generateAbbreviations('word')