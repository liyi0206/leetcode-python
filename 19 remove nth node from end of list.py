# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution(object):
    def removeNthFromEnd(self, head, n):
        """
        :type head: ListNode
        :type n: int
        :rtype: ListNode
        """
        if head == None: return None
        dummy = ListNode(0)
        dummy.next = head

        p,l = dummy,0
        while p.next: p,l = p.next,l+1
        
        start = dummy
        for i in range(l-n):
            start = start.next
            
        start.next = start.next.next
        return dummy.next
        
head=ListNode(1)
head.next=ListNode(2)
head.next.next=ListNode(3)
head.next.next.next=ListNode(4)
head.next.next.next.next=ListNode(5)
cur = head
while cur:
    print cur.val,
    cur=cur.next
print

a=Solution()
new=a.removeNthFromEnd(head,2)
cur = new
while cur:
#for i in range(10):
    print cur.val,
    cur=cur.next