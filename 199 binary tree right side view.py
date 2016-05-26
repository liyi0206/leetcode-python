# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution(object):
    def rightSideView(self, root):
        """
        :type root: TreeNode
        :rtype: List[int]
        """
        if root is None: return []
        q1,q2 = [root],[]
        res=[]
        while q1:
            res.append(q1[-1].val)
            for node in q1:
                if node.left: q2.append(node.left)
                if node.right:q2.append(node.right)
            q1,q2 = q2,[]
        return res
            
root = TreeNode(1)
root.left=TreeNode(2)
root.right=TreeNode(3)
root.left.right=TreeNode(5)
root.right.right=TreeNode(4)
a=Solution()
print a.rightSideView(root)