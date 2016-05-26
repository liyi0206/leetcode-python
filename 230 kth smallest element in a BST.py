# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution(object): #recursion
    def kthSmallest(self, root, k):
        """
        :type root: TreeNode
        :type k: int
        :rtype: int
        """
        if not root: return None
        self.k,self.i = k,0
        self.res=None
        self.dfs(root)
        return self.res
        
    def dfs(self,node):
        if node is None or self.res: return
        self.dfs(node.left)
        self.i+=1
        if self.i==self.k: 
            self.res=node.val
            return
        self.dfs(node.right)
     
class Solution2(object): #iteration
    def kthSmallest(self, root, k):
        stack,node=[],root
        i=0
        while stack or node:
            if node:
                stack.append(node)
                node=node.left
            else:
                parent=stack.pop()
                i+=1
                if i==k: return parent.val #return early when find
                node=parent.right
        
root=TreeNode(2)
root.left =TreeNode(1)
root.right=TreeNode(4)
root.right.left =TreeNode(3)
root.right.right=TreeNode(5)
      
a=Solution()
print a.kthSmallest(root,3)