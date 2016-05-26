### tree to double list ###
# three versions - preorder, inorder, level order
class TreeNode(object):
    def __init__(self,val):
        self.val=val
        self.left=None
        self.right=None
        
#inorder traversal, no need to be circular, no need to be double
class Solution1(object): # this method doesn't apply to preorder
    def flatten(self,root):       # not good, not generalizable
        if not root: return root
        stack=[]
        cur=root
        head=None
        pre =None
        while stack or cur:
            if cur:
                stack.append(cur)
                cur=cur.left
            else:
                parent = stack.pop()
                if pre: pre.right = parent #
                else: head = parent        #
                #parent.left = pre          #
                pre = parent               #
                cur = parent.right
        #tail = pre
        #tail.right,head.left = head,tail
        return head
  
class Solution2(object): # inorder, return head, could be generalized to preorder
    def flatten(self,root): # inorder cannot be in place!!!
        head,tail=self.helper(root)
        return head
    
    def helper(self,node):
        if not node: return None,None
    
        lh,lt = self.helper(node.left)
        rh,rt = self.helper(node.right)
        
        if lt: 
            node.left=lt
            lt.right= node
        if rh: 
            rh.left = node
            node.right =rh
    
        if lh: head=lh
        else: head = node
        if rt: tail=rt
        else: tail = node
        
        return head,tail
        
root=TreeNode(3)
root.left=TreeNode(2)
root.right=TreeNode(5)
root.left.left=TreeNode(1)
root.right.left=TreeNode(4)
root.right.right=TreeNode(6)

a=Solution1()
cur=a.flatten(root) #123456
while cur:
    print cur.val
    cur=cur.right
    
### not working yet ###
#class treeToListInorder3(object): 
#    def flatten(self,root):
#        self.last=None
#        self.recur(root)
#        
#    def recur(self,node): # change the node in place, and update self.last to be current node
#        if node== None: return
#        self.recur(node.right)
#        tmp=node.left
#        node.right= self.last
#        node.left = None
#        self.last = node
#        self.recur(tmp)