# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution(object):
    def recoverTree(self, root):
        """
        :type root: TreeNode
        :rtype: void Do not return anything, modify root in-place instead.
        """
        if root==None: return
        self.cur = None
        self.cand = []
        self.dfs(root)
                
        if len(self.cand)==1:
            self.cand[0][0].val,self.cand[0][1].val= \
            self.cand[0][1].val,self.cand[0][0].val
        else:
            self.cand[0][0].val,self.cand[1].val = \
            self.cand[1].val,self.cand[0][0].val
        
    def dfs(self, node):
        if node is None: return None
        
        self.dfs(node.left)
        
        if self.prev and self.prev.val>node.val:
            if len(self.cand)==0: self.cand.append([self.prev, node])
            else: self.cand.append(node)
        self.prev = node
        
        self.dfs(node.right)
    
