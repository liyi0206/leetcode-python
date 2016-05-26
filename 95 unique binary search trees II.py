# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution(object):
    def generateTrees(self, n):
        """
        :type n: int
        :rtype: List[TreeNode]
        """
        if n==0: return []
        return self.dfs(1, n)
        
    def dfs(self, low, high):
        res = []
        if low > high: res.append(None)
        for i in range(low, high+1):
            left = self.dfs(low, i-1)
            right =self.dfs(i+1, high)
            
            for j in left:
                for k in right:
                    current = TreeNode(i)
                    current.left = j
                    current.right= k
                    res.append(current)
        return res
        
a=Solution()
res = a.generateTrees(3)
print [a.val if a else None for a in res]