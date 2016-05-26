class Solution(object):
    def ladderLength(self, start, end, dict):
        """
        :type start: str
        :type end: str
        :type dict: Set[str]
        :rtype: int
        """
        res=0
        cur=[start]
        visited=set([start])
        dict.add(end)         ###
        while cur:
            nxt = []
            for word in cur:
                if word==end: return res+1
                for i in range(len(word)):
                    for c in 'abcdefghijklmnopqrstuvwxyz':
                        tmp = word[:i]+c+word[i+1:]
                        if tmp not in visited and tmp in dict:
                            nxt.append(tmp)
                            visited.add(tmp)
            res+=1
            cur=nxt
        return 0
        
a=Solution()
print a.ladderLength("hit","cog",set(["hot","dot","dog","lot","log"])) #5