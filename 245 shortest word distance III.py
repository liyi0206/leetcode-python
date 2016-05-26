class Solution(object):
    def shortestWordDistance(self, words, word1, word2):
        """
        :type words: List[str]
        :type word1: str
        :type word2: str
        :rtype: int
        """
        p1,p2=-1,-1
        res=1000000
        if word1==word2: 
            for i,w in enumerate(words):
                if w==word1:
                    if p1!=-1: res=min(res,i-p1)
                    p1=i
        else:
            for i,w in enumerate(words):
                if w==word1: p1=i
                if w==word2: p2=i
                if p1!=-1 and p2!=-1: res=min(res,abs(p1-p2))
        return res