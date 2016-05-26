class Solution(object):
    def findLadders(self, beginWord, endWord, wordlist):
        """
        :type beginWord: str
        :type endWord: str
        :type wordlist: Set[str]
        :rtype: List[List[int]]
        """
        wordlist.add(beginWord)
        wordlist.add(endWord)
        self.trace = {word:[] for word in wordlist}
        cur = set([beginWord]) 
        while cur and endWord not in cur:  ### o/w cannot break both for and while loop
            for word in cur: wordlist.remove(word)  ### for better efficiency
            nxt = set([])
            for word in cur:
                #if word==endWord: break
                for i in range(len(word)):
                    for c in 'abcdefghijklmnopqrstuvwxyz':
                        tmp = word[:i]+c+word[i+1:]
                        if tmp in wordlist:
                            self.trace[tmp].append(word)
                            nxt.add(tmp)
            cur = nxt
            
        self.res =[]
        if cur: self.bt([], endWord)
        return self.res
        
    def bt(self,path,word):
        if len(self.trace[word]) == 0: 
            self.res.append([word]+path)
            return
        for prev in self.trace[word]:
            self.bt([word]+path,prev)

a=Solution()
print a.findLadders("hit","cog",set(["hot","dot","dog","lot","log"]))
#[['hit', 'hot', 'lot', 'log', 'cog'], ['hit', 'hot', 'dot', 'dog', 'cog']]
