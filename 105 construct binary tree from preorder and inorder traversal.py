# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution(object):
    def buildTree(self, preorder, inorder):
        """
        :type preorder: List[int]
        :type inorder: List[int]
        :rtype: TreeNode
        """
        if len(inorder)==0 or len(preorder)==0: return None
         
        mid = inorder.index(preorder[0])
        cur = TreeNode(preorder.pop(0))
         
        cur.left = self.buildTree(preorder,inorder[:mid])
        cur.right= self.buildTree(preorder,inorder[mid+1:])
         
        return cur