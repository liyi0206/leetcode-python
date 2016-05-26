# Definition for binary tree with next pointer.
class TreeLinkNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None
        self.next = None

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
            
#You may only use constant extra space.
class Solution2(object):
    def connect(self, root):
        # head is used for locating next level's first node
        # tail is walking ahead until leval end
        cur=root
        tail=head=TreeLinkNode(0)
        while cur:
            # the two if clauses are both for first node in the level - the next level
            if cur.left:
                tail.next = cur.left # when tail.next points to sth, head.next also points to that
                tail=tail.next # when tail itself points to sth, itself walks away
            if cur.right:
                tail.next = cur.right
                tail=tail.next
                 
            # check whether cur to level end
            if cur.next:         # if not, continue
                cur = cur.next 
            else:                # if yes, reset
                cur = head.next
                tail = head      # tail itself
                tail.next = None # tail and head next both none
            
root=TreeLinkNode(1)
root.left=TreeLinkNode(2)
root.right=TreeLinkNode(3)
root.left.left=TreeLinkNode(4)
root.left.right=TreeLinkNode(5)
root.right.right=TreeLinkNode(7)

a=Solution2()
a.connect(root)
print root.left.next.val #3
print root.left.left.next.val #5
print root.left.right.next.val#7