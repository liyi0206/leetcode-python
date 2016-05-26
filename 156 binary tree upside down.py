# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution(object):
    def upsideDownBinaryTree(self, root):
        """
        :type root: TreeNode
        :rtype: TreeNode
        """
        if not root or not root.left or not root.right: return root
        newRoot=self.upsideDownBinaryTree(root.left)
        
        root.left.left=root.right
        root.left.right=root
        
        root.left=None
        root.right=None
        
        return newRoot
        
    def upsideDownBinaryTree2(self,root):
        cur=root
        pre=None
        nxt=None
        tmp=None
        while cur:
            nxt=cur.left
            cur.left=tmp
            cur.right=pre
            pre=cur
            cur=nxt
        return pre
        
root=TreeNode(1)
root.left=TreeNode(2)
root.right=TreeNode(3)
root.left.left=TreeNode(4)
root.left.right=TreeNode(5)

a=Solution()
new=a.upsideDownBinaryTree2(root)
print new.val
print new.left.val
print new.right.val
print new.right.left.val
print new.right.right.val