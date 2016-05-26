# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution(object):
    def partition(self, head, x):
        """
        :type head: ListNode
        :type x: int
        :rtype: ListNode
        """
        if head == None: return None
        l1 = ListNode(0)
        l2 = ListNode(0)
        
        p,p1,p2 = head,l1,l2
        while p:
            if p.val<x: 
                p1.next = p
                p1 = p1.next
            else: 
                p2.next = p
                p2 = p2.next
            p = p.next
            
        p2.next=None
        p1.next=l2.next
        return l1.next
        
head=ListNode(1)
head.next=ListNode(4)
head.next.next=ListNode(3)
head.next.next.next=ListNode(2)
head.next.next.next.next=ListNode(5)
head.next.next.next.next.next=ListNode(6)
cur = head
while cur:
    print cur.val,
    cur=cur.next
print

a=Solution()
new=a.partition(head,3)
cur = new
while cur:
#for i in range(10):
    print cur.val,
    cur=cur.next