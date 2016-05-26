# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution(object):
    #def postorderTraversal(self, root):
    #    """
    #    :type root: TreeNode
    #    :rtype: List[int]
    #    """
    #    self.res=[]
    #    self.postorder(root)
    #    return self.res
    #def postorder(self,root):
    #    if root is None:
    #        return
    #    self.postorder(root.left)
    #    self.postorder(root.right)
    #    self.res.append(root.val)
#iteration from wikipedia - logging version
    #def postorderTraversal(self, root):
    #    res, stack, node = [], [], root
    #    lastNodeVisited = None
    #    while stack or node:
    #        print "*** another round ***"
    #        if node is not None:
    #            stack.append(node)
    #            print "stack append ",node.val
    #            print "node.left ",node.left.val if node.left is not None else None
    #            node=node.left
    #            print "node ",node.val if node is not None else None
    #        else:
    #            peeknode=stack[-1]
    #            print "peeknode ",peeknode.val
    #            print "peeknode.right ",peeknode.right.val if peeknode.right is not None else None,", ",
    #            print "lastNodeVisited ",lastNodeVisited.val if lastNodeVisited is not None else None
    #            if peeknode.right is not None and lastNodeVisited is not peeknode.right:
    #                node=peeknode.right
    #                print "node ",node.val if node is not None else None
    #            else:
    #                res.append(peeknode.val)
    #                print "stack pop ",stack[-1].val
    #                lastNodeVisited = stack.pop()
    #                print "node not change ",node.val if node is not None else None,", ",
    #                print "lastNodeVisited ",lastNodeVisited.val if lastNodeVisited is not None else None
    #    return res
#iteration from wikipedia
    #def postorderTraversal(self, root):
    #    res, stack, node = [], [], root
    #    lastNodeVisited = None
    #    while stack or node:
    #        if node:
    #            stack.append(node)
    #            node=node.left
    #        else:
    #            peeknode=stack[-1]
    #            if peeknode.right and lastNodeVisited != peeknode.right:
    #                node=peeknode.right
    #            else:
    #                res.append(peeknode.val)
    #                lastNodeVisited = stack.pop()
    #    return res
#iteration from leetcode-py
    def postorderTraversal(self, root):
        res, stack, current, prev = [], [], root, None
        while stack or current:
            if current:
                stack.append(current)
                current = current.left
            else:
                parent = stack[-1]
                if parent.right in (None, prev):
                    prev = stack.pop()
                    res.append(prev.val)
                else:
                    current = parent.right
        return res


root=TreeNode(1)
root.right=TreeNode(2)
root.right.left=TreeNode(3)
a=Solution()
print a.postorderTraversal(root)