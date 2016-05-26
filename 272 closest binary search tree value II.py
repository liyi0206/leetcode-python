# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution(object):
    def closestKValues(self, root, target, k):
        """
        :type root: TreeNode
        :type target: float
        :type k: int
        :rtype: List[int]
        """
        self.tgt=target
        self.res=[]
        self.collect(root,k)
        return self.res
        
    def collect(self,root,k): #inorder traversal
        if not root: return
        
        self.collect(root.left,k)
        
        # as we inorder traverse, the smaller values are added first.
        # if abs(root.val-target)<abs(self.res[0]-target), it means -
        # the target is closer to the new value, res[0] is the first to pop.
        if len(self.res)==k:
            if abs(root.val-self.tgt)<abs(self.res[0]-self.tgt): 
                self.res=self.res[1:]
            else: return
        self.res.append(root.val)
        
        self.collect(root.right,k)
        
class Solution2(object):
    def closestKValues(self,root,target,k):
        cur=root
        stack=[]
        res1,res2=[],[]
        while stack or cur: 
            if cur:
                stack.append(cur) 
                cur=cur.left
            else:
                parent=stack.pop()
                if parent.val<=target:
                    res1.append(parent.val)     # res1 ascending
                else: res2.insert(0,parent.val) # res2 descending
                cur=parent.right
        res=[]
        for i in range(k):
            if not res1 and not res2: break #not going to happen
            # res 1 and not res2, or (res1 and res2 and ...<...)
            if not res2 or (res1 and target-res1[-1]<res2[-1]-target): 
                res.append(res1.pop())
            # not res1 and res2, or (res1 and res2 and ...>=...)
            else: res.append(res2.pop())
        return res


root=TreeNode(2)
root.left =TreeNode(1)
root.right=TreeNode(4)
root.right.left =TreeNode(3)
root.right.right=TreeNode(5)
a=Solution2()
print a.closestKValues(root,6,3)