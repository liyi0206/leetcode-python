# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution(object):
    def removeElements(self, head, val):
        """
        :type head: ListNode
        :type val: int
        :rtype: ListNode
        """
        if head == None: return None
        dummy = ListNode(0)
        dummy.next = head
        
        p = dummy
        while p.next:
            cur = p.next
            if cur.val == val:
                p.next = cur.next
            else:
                p = cur
        return dummy.next
        
node1,node2,node3,node4,node5,node6,node7 = ListNode(1),ListNode(2),ListNode(6),ListNode(3),ListNode(4),ListNode(5),ListNode(6)
nodes = [node1,node2,node3,node4,node5,node6,node7]
for i in range(len(nodes)-1):
    nodes[i].next = nodes[i+1]

cur = node1
while cur:
    print cur.val,
    cur=cur.next
print

a=Solution()
new = a.removeElements(node1,6)
cur = new
while cur:
    print cur.val,
    cur=cur.next