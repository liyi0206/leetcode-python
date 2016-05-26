# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution(object):
    #def lowestCommonAncestor(self, root, p, q):
    #    """
    #    :type root: TreeNode
    #    :type p: TreeNode
    #    :type q: TreeNode
    #    :rtype: TreeNode
    #    """
    #    self.p,self.q = p,q
    #    self.pathp,self.pathq=[],[]
    #    self.dfs(root,[])
    #    #print [a.val for a in self.pathp],[b.val for b in self.pathq]
    #    lp,lq=len(self.pathp),len(self.pathq)
    #    for i in range(min(lp,lq)):
    #        if self.pathp[i]!=self.pathq[i]:
    #            return self.pathp[i-1]
    #    return self.pathp[i]
    #            
    #def dfs(self,node,path):
    #    if node is None: return
    #    if node==self.p:
    #        self.pathp = path+[node]
    #    elif node==self.q:
    #        self.pathq = path+[node]
    #    self.dfs(node.left, path+[node])
    #    self.dfs(node.right,path+[node])
    
    def lowestCommonAncestor(self, root, p, q):
        #print "another dfs",root.val if root else None
        if not root or root==p or root==q: return root
        left =self.lowestCommonAncestor(root.left, p,q)
        #print "left", left.val if left else None
        right=self.lowestCommonAncestor(root.right,p,q)
        #print "right",right.val if right else None,"\n"
        if not left: return right
        elif not right: return left
        else: return root
                

node0,node1,node2 = TreeNode(0),TreeNode(1),TreeNode(2)
node3,node4,node5 = TreeNode(3),TreeNode(4),TreeNode(5)
node6,node7,node8 = TreeNode(6),TreeNode(7),TreeNode(8)

root=node3
root.left=node5
root.left.left =node6
root.left.right=node2
root.left.right.left =node7
root.left.right.right=node4
root.right=node1
root.right.left =node0
root.right.right=node8

a=Solution()
res=a.lowestCommonAncestor(root,node7,node4)
print res.val