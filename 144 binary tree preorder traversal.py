# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution1(object): # recursion
    def preorderTraversal(self, root):
        """
        :type root: TreeNode
        :rtype: List[int]
        """
        self.res=[]
        self.preorder(root)
        return self.res
    def preorder(self,root):
        if root is None: return
        self.res.append(root.val)
        self.preorder(root.left)
        self.preorder(root.right)
        
class Solution2(object): # iteration
    def preorderTraversal(self,root):
        res,stack,node = [],[],root
        while stack or node:
            if node:
                stack.append(node)
                res.append(node.val) # inorder, it is under else
                node=node.left
            else:
                parent=stack.pop()
                node=parent.right
        return res
        
        
root=TreeNode(2)
root.left=TreeNode(1)
root.right=TreeNode(4)
root.right.left=TreeNode(3)
root.right.right=TreeNode(5)
a=Solution2()
print a.preorderTraversal(root)