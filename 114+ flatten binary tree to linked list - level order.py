class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution(object):
    def flatten(self, root):
        if root is None: return
        cur= [root]
        tail=None
        while cur:
            nxt=[]
            if tail: tail.right=cur[0]
            while cur:
                node = cur.pop(0)
                if node.left: nxt.append(node.left)
                if node.right:nxt.append(node.right)
                
                node.left=None
                if cur: node.right=cur[0]
                tail=node
            cur=nxt
            
root=TreeNode(1)
root.left=TreeNode(2)
root.right=TreeNode(3)
root.left.left=TreeNode(4)
root.left.right=TreeNode(5)
root.right.left=TreeNode(6)
root.right.right=TreeNode(7)

a=Solution()
a.flatten(root) #1234567
cur=root
while cur: 
    print cur.val
    cur=cur.right