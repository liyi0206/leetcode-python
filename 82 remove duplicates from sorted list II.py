# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution(object):
    def deleteDuplicates(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        if head == None: return None
        dummy = ListNode(0)
        dummy.next = head
        
        front = dummy
        while front.next and front.next.next:
            if front.next.val == front.next.next.val:
                val = front.next.val
                p = front.next.next
                while p.next:
                    if p.next.val == val:
                        p = p.next
                    else: break
                front.next = p.next
            else:
                front = front.next     
        return dummy.next


head=ListNode(1)
head.next=ListNode(2)
head.next.next=ListNode(3)
head.next.next.next=ListNode(3)
head.next.next.next.next=ListNode(4)
head.next.next.next.next.next=ListNode(4)
head.next.next.next.next.next.next=ListNode(5)
cur = head
while cur:
    print cur.val,
    cur=cur.next
print

a=Solution()
new=a.deleteDuplicates(head)
cur = new
while cur:
    print cur.val,
    cur=cur.next