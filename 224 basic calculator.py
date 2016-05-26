class Solution(object):
    def calculate(self, s):
        """
        :type s: str
        :rtype: int
        """
        res=0
        stack= [] # store the res/sign before (
        number=0  # prev num
        sign=1    # prev sign
        for c in s:
            if c in "1234567890":
                number=10*number+int(c)
            elif c == "+":
                res+=sign*number
                number,sign=0,1
            elif c == "-":
                res+=sign*number
                number,sign=0,-1
            elif c == "(":
                stack.append(res)  #the res number before (
                stack.append(sign) #the sign before (
                sign,res=1,0 #indicate sign/num inside ()
            elif c == ")":
                res+=sign*number #the final res number inside ()
                number=0 # the number after )
                res*=stack.pop() #the sign before (
                res+=stack.pop() #the res number before (
        if number: res+=sign*number
        return res

                    
a=Solution()
print a.calculate("1 + 1")
print a.calculate("68 + 2")
print a.calculate("-(1+(4-5+2)+3)-(6+8)") #-19