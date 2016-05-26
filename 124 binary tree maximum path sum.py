# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution(object):
    def maxPathSum(self,root):
        """
        :type root: TreeNode
        :rtype: int
        """
        self.res=-1000000
        self.dfs(root)
        return self.res

    def dfs(self,root):
        if root is None: return 0
        left = self.dfs(root.left)
        right= self.dfs(root.right)
        cursum=max(left+root.val, right+root.val, root.val)
        curmax=max(cursum+right+root.val)
        self.res = max(curmax,self.res)
        return cursum
        
root=TreeNode(1)
root.left=TreeNode(2)
root.right=TreeNode(3)
a=Solution()
print a.maxPathSum(root)