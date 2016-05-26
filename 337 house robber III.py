# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution(object):
    def rob(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        return max(self.rec(root))
    def rec(self,root):
        if root is None: return (0,0) #rob, not rob
        l0,l1 = self.rec(root.left)
        r0,r1 = self.rec(root.right) 
        return (root.val+l1+r1,max(l1,l0)+max(r1,r0))
        
a=Solution()

root=TreeNode(3)
root.left=TreeNode(2)
root.right=TreeNode(3)
root.left.right=TreeNode(3)
root.right.right=TreeNode(1)
print a.rob(root) #7

root=TreeNode(3)
root.left=TreeNode(4)
root.right=TreeNode(5)
root.left.left =TreeNode(1)
root.left.right=TreeNode(3)
root.right.right=TreeNode(1)
print a.rob(root) #9