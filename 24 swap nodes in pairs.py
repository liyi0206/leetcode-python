# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution(object):
    def swapPairs(self, head):
        current = ListNode(0)
        current.next = head
        head = current
        while current.next and current.next.next:
            # pre-save the two, as they change after (1,2) swap
            next_one = current.next
            next_three = current.next.next.next 
            # (1,2) swap
            current.next = current.next.next
            current.next.next = next_one
            # re-link
            next_one.next = next_three
            # move 2 steps
            current = next_one
        return head.next
        
head=ListNode(1)
head.next=ListNode(2)
head.next.next=ListNode(3)
head.next.next.next=ListNode(4)
cur = head
for i in range(4):
    print cur.val,
    cur=cur.next
print

a=Solution()
new=a.swapPairs(head)
cur = new
for i in range(4):
    print cur.val,
    cur=cur.next