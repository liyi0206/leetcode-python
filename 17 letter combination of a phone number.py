class Solution(object):
    def letterCombinations(self, digits):
        """
        :type digits: str
        :rtype: List[str]
        """
        self.lookup=["", "", "abc", "def", "ghi", "jkl", \
                     "mno", "pqrs", "tuv", "wxyz"] #self.nums
        self.res=[]
        self.bt(digits,"") #word, or n
        return self.res
        
    def bt(self,digits,tmp): #void
        if digits == "":
            self.res.append(tmp)
            return
        for letter in self.lookup[int(digits[0])]:
            self.bt(digits[1:],tmp+letter)
        
a=Solution()
print a.letterCombinations("23")