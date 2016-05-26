class Solution(object):
    def maxProduct(self, words): # o(n) space, o(n^2) time
        """
        :type words: List[str]
        :rtype: int
        """
        nums = [0]*len(words) # a map for words, regarding the chars they use
        for ind,w in enumerate(words):
            for c in w:
                nums[ind] |= 1<<(ord(c)-ord('a'))
        #for num in nums: print bin(num)[2:].zfill(26)

        res = 0
        for x in range(len(words)):
            for y in range(x+1,len(words)):
                if (nums[x]&nums[y])==0:
                    res = max(res, len(words[x])*len(words[y]))

        return res
    
a=Solution()
print a.maxProduct(["abcw", "baz", "foo", "bar", "xtfn", "abcdef"])