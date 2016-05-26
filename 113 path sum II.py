# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution(object):
    def pathSum(self, root, sum):
        """
        :type root: TreeNode
        :type sum: int
        :rtype: List[List[int]]
        """
        self.target=sum
        self.paths=[]
        if root==None: return []
        self.dfs(root,[]) #void
        return self.paths
        
    def dfs(self,root,path):
        if root.left == None and root.right == None:
            if sum(path+[root.val])==self.target: 
                self.paths.append(path+[root.val])
            return
        if root.right:
            self.dfs(root.right,path+[root.val])
        if root.left:
            self.dfs(root.left, path+[root.val])

"""
    def pathSum(self, root, sum):
        return self.dfs([], root, sum)
        
    def dfs(self, res, path, root, sum):
        if root is None: return res
        if root.left is None and root.right is None and root.val == sum:
            return res + [path + [root.val]]
        return self.dfs(res,path+[root.val],root.left, sum-root.val)\
             + self.dfs(res,path+[root.val],root.right,sum-root.val)   
"""

root=TreeNode(5)
root.left=TreeNode(4)
root.right=TreeNode(8)
root.left.left=TreeNode(11)
root.right.left=TreeNode(13)
root.right.right=TreeNode(4)
root.left.left.left=TreeNode(7)
root.left.left.right=TreeNode(2)
root.right.right.left=TreeNode(5)
root.right.right.right=TreeNode(1)
a=Solution()
print a.pathSum(root, 22)