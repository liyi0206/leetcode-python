# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution(object):
    def countNodes(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        ct,lf,rt = 0,root,root
        while lf and rt:
            ct+=1 #h
            lf,rt = lf.left,rt.right
        if lf is None: return 2**ct-1
        return 1+self.countNodes(root.left)+self.countNodes(root.right)
        
    def countNodes2(self, root):        
        d=0
        node=root
        while node:
            d+=1
            node=node.left
        #print "d",d
        if d==0: return 0
        
        l,h=0,(1<<(d-1))-1
        while l<=h:
            m=(l+h)/2
            if self.getNode(root,m,d-1): l=m+1
            else: h=m-1
        return (1<<(d-1))+h
        
    def getNode(self,node,path,d):
        while d>0 and node:
            d-=1 
            if path&(1<<d): node=node.right
            else: node=node.left
        return node
        
root=TreeNode(1)
root.left =TreeNode(2)
root.right=TreeNode(3)
root.left.left =TreeNode(4)
root.left.right=TreeNode(5)
a=Solution()
print a.countNodes2(root)