class Solution(object):
    def evalRPN(self, tokens):
        """
        :type tokens: List[str]
        :rtype: int
        """
        #def RepresentsInt(s):
        #    try: 
        #        int(s)
        #        return True
        #    except ValueError:
        #        return False
                
        stack=[]
        for x in tokens:
            if x[0] in "1234567890" or (len(x)>1 and x[1] in "1234567890"): #neg
                stack.append(int(x))
            elif x=="+": stack.append(stack.pop()+stack.pop())#;print stack[-1]
            elif x=="-": 
                num2=stack.pop()
                stack.append(stack.pop()-num2)#;print stack[-1]
            elif x=="*": stack.append(stack.pop()*stack.pop())#;print stack[-1]
            elif x=="/": 
                num2=stack.pop()
                num1=stack.pop()
                sign=-1 if (num1<0)^(num2<0) else 1
                stack.append(abs(num1)/abs(num2)*sign)#;print stack[-1]
        return stack[0]
        
        
a=Solution()
print a.evalRPN(["2", "1", "+", "3", "*"])
print a.evalRPN(["4", "13", "5", "/", "+"])
print a.evalRPN(["0","3","/"])
print a.evalRPN(["10","6","9","3","+","-11","*","/","*","17","+","5","+"])