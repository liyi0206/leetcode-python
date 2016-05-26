# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution1(object): # recursion
    def inorderTraversal(self, root):
        """
        :type root: TreeNode
        :rtype: List[int]
        """
        self.res=[]
        self.inorder(root)
        return self.res
        
    def inorder(self,root):
        if root is None: return
        self.inorder(root.left)
        self.res.append(root.val)
        self.inorder(root.right)

class Solution2(object): # iteration
    def inorderTraversal(self, root):
        cur=root
        stack=[]
        res=[]
        while stack or cur: # anything in stack is considered as parent
            if cur:
                stack.append(cur) # add to stack
                cur=cur.left
            else:
                parent=stack.pop() # pop from stack
                res.append(parent.val) ### the only place to add to res
                cur=parent.right
        return res

root=TreeNode(2)
root.left=TreeNode(1)
root.right=TreeNode(4)
root.right.left=TreeNode(3)
root.right.right=TreeNode(5)

a=Solution2()
print a.inorderTraversal(root)
