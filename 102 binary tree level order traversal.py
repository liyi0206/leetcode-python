# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution(object):
    def levelOrder(self, root):
        """
        :type root: TreeNode
        :rtype: List[List[int]]
        """
        if root is None: return []
        cur, res = [root], []
        while cur:
            nxt, vals = [], []
            for node in cur:
                vals.append(node.val)
                if node.left: nxt.append(node.left)
                if node.right:nxt.append(node.right)
            res.append(vals)
            cur = nxt
        return res
        
root=TreeNode(3)
root.left =TreeNode(9)
root.right=TreeNode(20)
root.right.left =TreeNode(15)
root.right.right=TreeNode(7)

a=Solution()
print a.levelOrder(root)