# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

#class Solution(object):
#    def zigzagLevelOrder(self, root):
#        """
#        :type root: TreeNode
#        :rtype: List[List[int]]
#        """
#        if root == None: return []
#        res, current, reverse = [], [root], 0
#        while len(current) > 0:
#                vals = []
#                for i in range(len(current)):
#                    this_node = current[0]
#                    if reverse: vals.insert(0, this_node.val)
#                    else: vals.append(this_node.val)
#                    if this_node.left != None: current.append(this_node.left)
#                    if this_node.right!= None: current.append(this_node.right)
#                    current.pop(0)
#                res.append(vals)
#                reverse = 1-reverse
#        return res

class Solution(object):
    def zigzagLevelOrder(self, root):
        if root==None: return []
        res, current, reverse = [], [root], 0
        while current:
            vals,next = [],[]
            for node in current:
                if reverse: vals.insert(0, node.val)
                else: vals.append(node.val)
                if node.left is not None: next.append(node.left)
                if node.right is not None:next.append(node.right)
            res.append(vals)
            current=next
            reverse = 1-reverse
        return res
        
root=TreeNode(3)
root.left=TreeNode(9)
root.right=TreeNode(20)
root.right.left=TreeNode(15)
root.right.right=TreeNode(7)
a=Solution()
print a.zigzagLevelOrder(root)