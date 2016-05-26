# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution(object):
    def reverseKGroup(self, head, k):
        """
        :type head: ListNode
        :type k: int
        :rtype: ListNode
        """
        dummy = ListNode(0)
        dummy.next=head
        p,l = head,0
        while p: p,l = p.next,l+1
        start,ind = dummy,0
        
        while start:
            if (l-ind)/k == 0: break
            front=start.next
            tmp = front
            for i in range(k):
                tmp1 = front.next
                tmp2 = start.next
                start.next = front
                start.next.next = tmp2
                front = tmp1
            tmp.next = front
            start,ind = tmp,ind+k
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
new=a.reverseKGroup(head,2)
cur = new
while cur:
    print cur.val,
    cur=cur.next

# the old head is destroyed!
#cur = head
#while cur:
#    print cur.val,
#    cur=cur.next

#new=a.reverseKGroup(head,3)
#cur = new
#while cur:
#    print cur.val,
#    cur=cur.next