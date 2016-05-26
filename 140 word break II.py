class Solution(object):
    def wordBreak(self, s, wordDict):
        """
        :type s: str
        :type wordDict: Set[str]
        :rtype: List[str]
        """
        prev= [[] for i in range(len(s)+1)]
        s = '0'+s
        for i in range(len(s)):
            if i==0 or len(prev[i])>0:
                for word in wordDict:
                    if i+len(word)<=len(s) and word==s[i+1:i+len(word)+1]:
                        prev[i+len(word)].append(i)
        self.s,self.prev,self.res = s,prev,[]
        if len(prev[-1])>0: self.bt(len(s)-1,[])
        return self.res
        
    def bt(self,idx,path):
        if idx == 0: self.res.append(' '.join(path))
        for m in self.prev[idx]:
            self.bt(m,[self.s[m+1:idx+1]]+path)


a=Solution()
print a.wordBreak("catsanddog",["cat", "cats", "and", "sand", "dog"])