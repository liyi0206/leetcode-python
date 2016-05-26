# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution(object):
    def reverseBetween(self, head, m, n):
        """
        :type head: ListNode
        :type m: int
        :type n: int
        :rtype: ListNode
        """
        if head == None: return None
        dummy = ListNode(0)
        dummy.next = head
        
        start = dummy
        for i in range(m-1):
            start = start.next
        #print "start",start.val
            
        front = start.next
        tmp = front
        for i in range(n-m+1):
            tmp1=front.next
            tmp2=start.next
            start.next = front
            start.next.next = tmp2
            front=tmp1
        #print "front",front.val
            
        tmp.next = front
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
new=a.reverseBetween(head,1,4)
cur = new
while cur:
    print cur.val,
    cur=cur.next
        