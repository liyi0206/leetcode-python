class Solution(object):
    def removeInvalidParentheses(self, s): #o(n!)
        """
        :type s: str
        :rtype: List[str]
        """
        self.visited=set([s])
        self.res=[]
        self.bt(s)
        return self.res
        
    def bt(self,s):
        tmp=self.calc(s)#;print tmp
        if tmp==0: self.res.append(s)
        for i in range(len(s)):
            if s[i] in "()":
                ns=s[:i]+s[i+1:]
                if ns not in self.visited and self.calc(ns)<tmp:
                    self.visited.add(ns)
                    self.bt(ns)
        
    def calc(self,s):
        a,b=0,0
        stack=[]
        for c in s:
            if c=="(": stack.append(c)
            elif c==")": 
                if not stack: b+=1
                else: stack.pop()
        a+=len(stack)
        return a+b
        
a=Solution()
print a.removeInvalidParentheses("()())()") #["()()()", "(())()"]
print a.removeInvalidParentheses("(a)())()") #["(a)()()", "(a())()"]
print a.removeInvalidParentheses(")(") #[""]

print a.removeInvalidParentheses(")(f") #["f"]