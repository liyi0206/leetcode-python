# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution(object):
    def lowestCommonAncestor(self, root, p, q):
        """
        :type root: TreeNode
        :type p: TreeNode
        :type q: TreeNode
        :rtype: TreeNode
        """
        cur=root
        while cur:
            if p.val<cur.val and q.val<cur.val:
                cur=cur.left
            elif p.val>cur.val and q.val>cur.val:
                cur=cur.right
            else: return cur
        
root=TreeNode(6)
node2=TreeNode(2)
node4=TreeNode(4)
node8=TreeNode(8)

root.left=node2
root.left.left =TreeNode(0)
root.left.right=node4
root.left.right.left =TreeNode(3)
root.left.right.right=TreeNode(5)
root.right=node8
root.right.left =TreeNode(7)
root.right.right=TreeNode(9)

a=Solution()
res1=a.lowestCommonAncestor(root,node2,node8)
print res1.val #6
res2=a.lowestCommonAncestor(root,node2,node4)
print res2.val #2