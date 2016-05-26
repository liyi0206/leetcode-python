# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution(object):
    def closestValue(self, root, target): # get closest value
        """
        :type root: TreeNode
        :type target: float
        :rtype: int
        """
        res=root.val
        cur=root
        while cur:
            if target==cur.val: return cur.val
            if abs(target-cur.val)<abs(target-res): res=cur.val
            if target>cur.val: cur=cur.right
            else: cur=cur.left
        return res

root=TreeNode(2)
root.left =TreeNode(1)
root.right=TreeNode(4)
root.right.left =TreeNode(3)
root.right.right=TreeNode(5)

a=Solution()
print a.closestValue(root,3.3) #3
print a.closestValue(TreeNode(0),5) #0
                       
class Solution2(object):
    def closestValue(self, root, target): # get closest diff
        if not root: return None
        if root.val==target: return 0
        elif root.val<target: 
            closest=self.closestValue(root.right,target)
        else:
            closest=self.closestValue(root.left, target)
        res=target-root.val
        if closest and abs(closest)<abs(res): return closest
        return res

#a=Solution2()
#print a.closestValue(root,3.3) #0.3