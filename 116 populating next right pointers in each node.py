# Definition for binary tree with next pointer.
class TreeLinkNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None
        self.next = None

# perfect binary tree (ie, all leaves are at the same level, 
# and every parent has two children).
class Solution(object):
    def connect(self, root):
        """
        :type root: TreeLinkNode
        :rtype: nothing
        """
        if root is None: return
        cur= [root]
        while cur:
            nxt=[]
            while cur:
                node = cur.pop(0)
                if cur: node.next = cur[0]
                if node.left: nxt.append(node.left)
                if node.right:nxt.append(node.right)
            cur=nxt
      
# You may only use constant extra space.      
class Solution2(object):
    def connect(self, root):
        cur = root
        while cur:
            pre = cur ###
            while cur:
                if cur.left:
                    cur.left.next = cur.right
                if cur.right and cur.next:
                    cur.right.next = cur.next.left
                cur = cur.next # at last, right most is none (not exist)
            cur = pre.left ###
            
root=TreeLinkNode(1)
root.left=TreeLinkNode(2)
root.right=TreeLinkNode(3)
root.left.left=TreeLinkNode(4)
root.left.right=TreeLinkNode(5)
root.right.left=TreeLinkNode(6)
root.right.right=TreeLinkNode(7)

a=Solution()
a.connect(root)
print root.left.next.val #3
print root.left.left.next.val #5
print root.left.right.next.val#6
print root.right.left.next.val#7