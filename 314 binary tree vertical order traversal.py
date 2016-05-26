# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution(object):            #hash table
    def verticalOrder(self, root): #BFS - keep the orders (left to right, top to bottom)
        """
        :type root: TreeNode
        :rtype: List[List[int]]
        """
        if not root: return []
        mp={}
        cur=[(0,root)]
        min_idx,max_idx=100000,-100000
        while cur:
            nxt=[]
            for idx,node in cur:
                min_idx=min(min_idx,idx)
                max_idx=max(max_idx,idx)
                if idx not in mp: mp[idx]=[node.val]
                else: mp[idx].append(node.val)
                if node.left: nxt.append((idx-1,node.left))
                if node.right: nxt.append((idx+1,node.right))
            cur=nxt
        return [mp[k] for k in range(min_idx,max_idx+1)]
 
    def verticalOrder2(self, root): #easier to sort keys
        if not root: return []
        mp={}
        cur=[(0,root)]
        while cur:
            nxt=[]
            for idx,node in cur:
                if idx not in mp: mp[idx]=[node.val]
                else: mp[idx].append(node.val)
                if node.left: nxt.append((idx-1,node.left))
                if node.right: nxt.append((idx+1,node.right))
            cur=nxt
        return [mp[k] for k in sorted(mp.keys())]

root=TreeNode(3)
root.left=TreeNode(9)
root.right=TreeNode(20)
root.right.left=TreeNode(15)
root.right.right=TreeNode(7)

a=Solution()
print a.verticalOrder2(root)