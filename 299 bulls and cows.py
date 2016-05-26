class Solution(object):
    def getHint(self, secret, guess):
        """
        :type secret: str
        :type guess: str
        :rtype: str
        """
        num1,num2=0,0
        tmp1,tmp2=[],[]
        for i in range(len(secret)):
            if secret[i]==guess[i]: num1+=1
            else: 
                tmp1.append(secret[i])
                tmp2.append(guess[i])
        for c in tmp1:
            if c in tmp2:
                tmp2.remove(c)
                num2+=1
        return str(num1)+"A"+str(num2)+"B"
        
a=Solution()
print a.getHint("9305","1234")
print a.getHint("9305","5678")
print a.getHint("9305","9012")
print a.getHint("9305","9087")
print a.getHint("9305","1087")
print a.getHint("9305","9205")
print a.getHint("9305","9305")