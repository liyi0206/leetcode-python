# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution(object):
    def levelOrderBottom(self, root):
        """
        :type root: TreeNode
        :rtype: List[List[int]]
        """
        if root is None: return []
        res, current = [], [root]
        while current:
            next, vals = [], []
            for node in current:
                vals.append(node.val)
                if node.left: next.append(node.left)
                if node.right:next.append(node.right)
            current = next
            res.insert(0, vals)
        return res
            
root=TreeNode(3)
root.left =TreeNode(9)
root.right=TreeNode(20)
root.right.left =TreeNode(15)
root.right.right=TreeNode(7)

a=Solution()
print a.levelOrderBottom(root)