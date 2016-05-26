# Definition for a binary tree node
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class BSTIterator(object):
    def __init__(self, root):
        """
        :type root: TreeNode
        """
        self.stack=[]
        self.cur=root

    def hasNext(self):
        """
        :rtype: bool
        """
        return self.stack or self.cur

    def next(self):
        """
        :rtype: int
        """
        while self.cur or self.stack:
            if self.cur:
                self.stack.append(self.cur)
                self.cur=self.cur.left
            else:
                parent = self.stack.pop()
                self.cur = parent.right
                return parent.val


root=TreeNode(2)
root.left=TreeNode(1)
root.right=TreeNode(4)
root.right.left=TreeNode(3)
root.right.right=TreeNode(5)

i,v = BSTIterator(root),[]
while i.hasNext(): v.append(i.next())
print v