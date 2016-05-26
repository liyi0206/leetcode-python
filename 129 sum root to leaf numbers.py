# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution(object):
#    def sumNumbers(self, root):
#        """
#        :type root: TreeNode
#        :rtype: int
#        """
#        if root==None: return 0
#        return self.dfs(root, 0)
#
#    def dfs(self, root, sum):
#        if root.left == None and root.right == None:
#            return 10*sum+root.val
#        elif root.left==None and root.right:
#            return self.dfs(root.right,10*sum+root.val)
#        elif root.left and root.right==None:
#            return self.dfs(root.left, 10*sum+root.val)
#        else: 
#            return self.dfs(root.left, 10*sum+root.val) + \
#                   self.dfs(root.right,10*sum+root.val)

    def sumNumbers(self, root):
        if root==None: return 0
        self.res=0
        self.dfs(root, 0)
        return self.res

    def dfs(self, root, sum):
        print "sum",sum
        if root.left == None and root.right == None:
            self.res += 10*sum+root.val
        if root.left:
            self.dfs(root.left, 10*sum+root.val)
            print "done with left, sum",sum
        if root.right:
            self.dfs(root.right,10*sum+root.val)
            print "done with right, sum",sum

root=TreeNode(1)
root.left=TreeNode(2)
root.right=TreeNode(3)
a=Solution()
print a.sumNumbers(root)