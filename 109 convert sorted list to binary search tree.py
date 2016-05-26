# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None

# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution(object):
    def sortedListToBST(self, head):
        """
        :type head: ListNode
        :rtype: TreeNode
        """
        L,cur=0,head
        while cur:
            L+=1
            cur=cur.next
        self.cur=head
        return self.dfs(L)
    
    def dfs(self,L):
        if L<=0: return None
        left = self.dfs(L/2)
        root = ListNode(self.cur.val)
        
        self.cur = self.cur.next
        
        right = self.dfs(L-L/2-1)
        root.left = left
        root.right = right
        return root

#head=ListNode(3) 
#head.next=ListNode(5)
#head.next.next=ListNode(8)
#
#a=Solution()
#root=a.sortedListToBST(head)
#print root.val
#print root.left.val
#print root.right.val

head=ListNode(1) 
head.next=ListNode(3)

a=Solution()
root=a.sortedListToBST(head)
print root.val
print root.left.val
print root.right