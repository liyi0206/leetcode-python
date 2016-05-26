# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution(object):
    def hasPathSum(self, root, sum):
        """
        :type root: TreeNode
        :type sum: int
        :rtype: bool
        """
        self.target=sum
        self.res = False
        if root==None: return False
        self.dfs(root,[]) #void
        return self.res
        
    def dfs(self,root,path):
        if root.left == None and root.right == None:
            if sum(path+[root.val])==self.target: self.res=True
            return
        if root.right:
            self.dfs(root.right,path+[root.val])
        if root.left:
            self.dfs(root.left, path+[root.val])

"""
    def hasPathSum(self, root, sum):
        if root is None: return False
        if root.left is None and root.right is None and sum == root.val:
            return True
        return self.hasPathSum(root.left, sum-root.val) or \
               self.hasPathSum(root.right,sum-root.val)
"""
                  
root=TreeNode(5)
root.left=TreeNode(4)
root.right=TreeNode(8)
root.left.left=TreeNode(11)
root.right.left=TreeNode(13)
root.right.right=TreeNode(4)
root.left.left.left=TreeNode(7)
root.left.left.right=TreeNode(2)
root.right.right.right=TreeNode(1)
a=Solution()
print a.hasPathSum(root, 22)
