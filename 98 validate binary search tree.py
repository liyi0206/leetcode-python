# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution(object):
    def isValidBST(self, root):
        """
        :type root: TreeNode
        :rtype: bool
        """
        import sys
        return self.dfs(root,sys.maxint,-sys.maxint-1)
        
    def dfs(self, root, upper, lower):
        if root is None: return True
        if root.val <= lower or root.val >= upper: return False
        return self.dfs(root.left, root.val, lower) and \
               self.dfs(root.right,upper, root.val)
        


root=TreeNode(2)
root.left=TreeNode(1)
root.right=TreeNode(3)
a=Solution()
print a.isValidBST(root)