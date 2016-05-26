class Solution(object):
    def calculate(self, s):
        """
        :type s: str
        :rtype: int
        """
        if not s: return 0
        stack=[]
        number,sign=0,"+"
        for i,c in enumerate(s):
            if c in "1234567890": number=number*10+int(c)
            if c in "+-*/" or i==len(s)-1:
                if sign=="+": stack.append(number)
                if sign=="-": stack.append(-number)
                if sign=="*": stack.append(stack.pop()*number)
                if sign=="/": 
                    num1=stack.pop()
                    tmp=-1 if (num1<0)^(number<0) else 1
                    stack.append(abs(num1)/abs(number)*tmp)
                number,sign = 0,c
        return sum(stack)
        
a=Solution()
print a.calculate("3+2*2")
print a.calculate(" 3/2 ")
print a.calculate(" 3+5 / 2 ")
print a.calculate("14-3/2")