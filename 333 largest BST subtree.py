# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution(object):
    def largestBSTSubtree(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        return self.dfs(root)[0]
        
    def dfs(self,root):
        #N is the size of the largest BST in the tree.
        #If the tree is a BST, then n is the number of nodes, otherwise it's -infinity.
        #If the tree is a BST, then min and max are the minimum/maximum value in the tree.
        
        if not root: return 0,0,float('inf'),float('-inf')
        N1,n1,min1,max1 = self.dfs(root.left)
        N2,n2,min2,max2 = self.dfs(root.right)
        n=1+n1+n2 if max1<root.val<min2 else float('-inf')
        return max(N1,N2,n),n,min(min1,root.val),max(max2,root.val)   

root=TreeNode(10)
root.left=TreeNode(5)
root.right=TreeNode(15)
root.left.left=TreeNode(1)
root.left.right=TreeNode(8)
root.right.right=TreeNode(7)

a=Solution()
print a.largestBSTSubtree(root)