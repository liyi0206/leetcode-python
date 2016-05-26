# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution(object):
    def oddEvenList(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        if not head: return None
        front=head.next
        cur=head
        while cur and cur.next and cur.next.next:
            next_one=cur.next
            cur.next=cur.next.next
            next_one.next=cur.next.next
            cur=cur.next
        if cur.next: cur.next=None
        cur.next=front
        return head
        
head1=ListNode(1)
head1.next=ListNode(2)
head1.next.next=ListNode(3)
a=Solution()
new=a.oddEvenList(head1)
while new:
    print new.val
    new=new.next