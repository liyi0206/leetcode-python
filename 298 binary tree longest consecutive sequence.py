# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution(object):
    def longestConsecutive(self, root): #DFS
        """
        :type root: TreeNode
        :rtype: int
        """
        self.res=0
        self.dfs(root,None,0)
        return self.res
        
    def dfs(self,node,prev,num):
        #print node.val if node else None,prev.val if prev else None,num
        if not node: 
            self.res=max(self.res,num)#;print "None. res",self.res
            return
        if not prev or prev.val+1==node.val: 
            self.dfs(node.left,node,num+1)
            self.dfs(node.right,node,num+1)
        else:
            self.res=max(self.res,num)#;print "Restart. res",self.res
            self.dfs(node.left,node,1)
            self.dfs(node.right,node,1)    
            
root1=TreeNode(1)
root1.right=TreeNode(3)
root1.right.left=TreeNode(2)
root1.right.right=TreeNode(4)
root1.right.right.right=TreeNode(5)
            
root2=TreeNode(2)
root2.right=TreeNode(3)
root2.right.left=TreeNode(2)
root2.right.left.left=TreeNode(1)

a=Solution()
print a.longestConsecutive(root1) #3
print a.longestConsecutive(root2) #2