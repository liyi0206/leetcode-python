# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution(object):
    def buildTree(self, inorder, postorder):
        """
        :type inorder: List[int]
        :type postorder: List[int]
        :rtype: TreeNode
        """
        if len(inorder)==0 or len(postorder)==0: return None
         
        mid = inorder.index(postorder[-1])
        cur = TreeNode(postorder.pop())
         
        cur.right= self.buildTree(inorder[mid+1:],postorder)
        cur.left = self.buildTree(inorder[:mid],postorder)
         
        return cur
        
a=Solution()
tree_node = a.buildTree([1,2,3,4],[1,4,3,2])