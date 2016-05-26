class Solution(object):
    def isValidSerialization(self, preorder):
        """
        :type preorder: str
        :rtype: bool
        """
        stack=[]
        for item in preorder.split(','):
            stack.append(item)
            while len(stack)>=3 and stack[-3] != '#' \
                   and stack[-2] == stack[-1] == '#':
                stack.pop();stack.pop();stack.pop()
                stack.append("#")
        return stack==["#"]
        
a=Solution()
print a.isValidSerialization("9,3,4,#,#,1,#,#,2,#,6,#,#")
print a.isValidSerialization("1,#")
print a.isValidSerialization("9,#,#,1")