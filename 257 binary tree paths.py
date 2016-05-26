# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution(object):
    def binaryTreePaths(self, root):
        """
        :type root: TreeNode
        :rtype: List[str]
        """
        if not root: return []
        self.res=[]
        self.dfs(root,[])
        return self.res
        
    def dfs(self,root,path):
        if not root.left and not root.right:
            self.res.append("->".join(path+[str(root.val)]))
        if root.right:self.dfs(root.right,path+[str(root.val)])
        if root.left: self.dfs(root.left, path+[str(root.val)])
            
root=TreeNode(1)
root.left=TreeNode(2)
root.right=TreeNode(3)
root.left.right=TreeNode(5)
a=Solution()
print a.binaryTreePaths(root)