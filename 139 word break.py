class Solution(object):
    def wordBreak(self, s, wordDict):
        """
        :type s: str
        :type wordDict: Set[str]
        :rtype: bool
        """
        dp = [True]+[False]*len(s)
        s = '0'+s
        for i in range(len(s)):
            if dp[i]:
                for word in wordDict:
                    if i+len(word)<=len(s) and word==s[i+1:i+1+len(word)]:
                        if i+len(word)==len(s)-1: return True
                        else: dp[i+len(word)]=True
        #print dp
        return dp[-1]
        
a=Solution()
print a.wordBreak("catsanddog",["cat", "cats", "and", "sand", "dog"])