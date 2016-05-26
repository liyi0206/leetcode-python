# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution(object):
    # BFS - use queue/heap, take less space
    def invertTree(self, root):
        """
        :type root: TreeNode
        :rtype: TreeNode
        """
        if root is None: return root
        q1,q2 = [root],[]
        while q1:
            print [a.val for a in q1]
            while q1:
                a = q1.pop(0)
                #print a.val,a.left.val if a.left.val else None,a.right.val if a.right.val else None
                a.left,a.right = a.right,a.left                
                if a.left: q2.append(a.left)
                if a.right:q2.append(a.right)
            q1,q2 = q2,[]
        return root
        
    # DFS - use stack, take more space
    def invertTree2(self,root):
        if root is None: return root
        root.left,root.right = self.invertTree(root.right),self.invertTree(root.left)
        return root
        
root=TreeNode(4)
root.left=TreeNode(2)
root.left.left=TreeNode(1)
root.left.right=TreeNode(3)
root.right=TreeNode(7)
#root.right.left=TreeNode(6)
root.right.right=TreeNode(9)

a=Solution()
new=a.invertTree(root)
print new.val,new.left.val,new.right.val,
print new.left.left.val, new.left.right,#.val,
print new.right.left.val,new.right.right.val