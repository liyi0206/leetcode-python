# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution(object): # preorder, in place
    last = None
    def flatten(self, root):
        """
        :type root: TreeNode
        :rtype: void Do not return anything, modify root in-place instead.
        """
        if root != None:
            self.flatten(root.right)
            self.flatten(root.left)
            root.right = self.last
            root.left = None
            self.last = root
            
class Solution1(object): # preorder, in place
    def flatten(self, root):
        self.last=None
        self.recur(root)
        
    def recur(self,node):
        if node== None: return
        self.recur(node.right)
        self.recur(node.left)
        node.right= self.last
        node.left = None
        self.last = node

class Solution2(object): #preorder, in place, could be generalized to be inorder
    def flatten(self, root):
        self.helper(root)

    def helper(self,node):
        if not node: return None,None
    
        lh,lt = self.helper(node.left)
        rh,rt = self.helper(node.right)

        if lt: 
            node.right = lh
            lt.right = rh  
        else: node.right = rh
    
        if rt: tail = rt
        elif lt: tail = lt
        else: tail = node
        
        node.left = None
        
        return node,tail
        
root=TreeNode(3)
root.left=TreeNode(2)
root.right=TreeNode(5)
root.left.left=TreeNode(1)
root.right.left=TreeNode(4)
root.right.right=TreeNode(6)       
                      
a=Solution2()
a.flatten(root)
cur=root
while cur:
    print cur.val
    cur=cur.right
    
## wrong direction
#def treeToList2(root): 
#    if not root: return root
#    stack=[]
#    cur=root
#    head=None
#    pre =None
#    while stack or cur:
#        if cur:
#           if pre: pre.right = cur #
#           else: head = cur        #
#           pre = cur               #
#           
#           stack.append(cur) ## actually put pre to stack, so wrong
#           cur=cur.left
#        else:
#           parent=stack.pop()
#           cur=parent.right
#    return head