# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution(object):
    def isBalanced(self, root):
        """
        :type root: TreeNode
        :rtype: bool
        """
        return self.dfs(root) != -1
    # given -1, it is good for early return, if already -1
    def dfs(self, root):
        if root == None: return 0
        h1 = self.dfs(root.left)
        if h1 ==-1: return -1
        h2= self.dfs(root.right) 
        if h2 ==-1 or abs(h1-h2)>1: return -1
        return max(h1,h2) + 1
        
    #logging version    
    #def dfs(self, root):
    #    print "another dfs with",root.val if root is not None else None
    #    if root == None: return 0
    #    h1 = self.dfs(root.left)
    #    print "done with left of",root.val,"h1=",h1
    #    if h1<0: 
    #        print "return -1"
    #        return -1
    #    h2= self.dfs(root.right) 
    #    print "done with right of",root.val,"h2=",h2
    #    if h2 < 0 or abs(h1-h2) > 1:
    #        print "done with compare, return -1"
    #        return -1
    #    print "done with compare, return",max(h1, h2)+1,"\n"
    #    return max(h1, h2) + 1

    # a clear solution that set flag and height apart - but no early return!
    #def isBalanced(self, root):
    #    self.flag=True
    #    print self.dfs(root)
    #    return self.flag
    #
    #def dfs(self, root):
    #    if root == None: return 0
    #    h1,h2 = 0,0
    #    if root.left: h1=self.dfs(root.left)
    #    print "done with left of",root.val
    #    if root.right:h2=self.dfs(root.right)
    #    print "done with right of",root.val
    #    if abs(h1-h2)>1: 
    #        print h1,h2,"flag false"
    #        self.flag=False
    #    return max(h1,h2)+1
        
        
root=TreeNode(1)
root.left=TreeNode(21)
root.right=TreeNode(22)
root.left.left=TreeNode(31)
root.left.right=TreeNode(32)
root.right.left=TreeNode(33)
root.left.left.left=TreeNode(41)

a=Solution()
print a.isBalanced(root)