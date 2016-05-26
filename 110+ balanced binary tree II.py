# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution(object):
    def isBalanced(self, root):
        """
        :type root: TreeNode
        :rtype: bool
        """
        import sys
        if root==None: return True
        self.min,self.max = sys.maxint,-1
        return self.dfs(root,1)
        
    def dfs(self,root,dp):
        #if root is None:  
        #    self.min = min(self.min,dp)
        #    print self.min,
        #    self.max = max(self.max,dp)
        #    print self.max
        #    if self.min+1<self.max: return False
        #    else: return True
        if not root.left and not root.right:
            self.min = min(self.min,dp)
            self.max = max(self.max,dp)
            if self.min+1<self.max: return False
            else: return True
        elif root.left and not root.right:
            return self.dfs(root.left,dp+1)
        elif root.right and not root.left:
            return self.dfs(root.right,dp+1)
        return self.dfs(root.left,dp+1) and self.dfs(root.right,dp+1)
        
root=TreeNode(1)
root.left=TreeNode(2)
root.right=TreeNode(2)
root.left.left=TreeNode(3)
root.left.right=TreeNode(3)
root.right.left=TreeNode(3)
root.left.left.left=TreeNode(4)

a=Solution()
print a.isBalanced(root)