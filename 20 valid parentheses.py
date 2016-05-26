class Solution(object):
    def isValid(self, s):
        mp={'(':')', '{':'}', '[':']'}
        stack=[]
        for c in s:
            if c in mp: stack.append(c)
            ### remember not stack
            elif not stack or mp[stack.pop()]!=c: return False
        if stack: return False
        return True
        
a=Solution()
print a.isValid("()[]{}")
print a.isValid("([)]")