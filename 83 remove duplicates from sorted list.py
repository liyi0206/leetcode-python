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
        
        front = head
        while front.next:
            if front.next.val == front.val:
                front.next = front.next.next
            else:
                front = front.next     
        return dummy.next
        
        
head=ListNode(1)
head.next=ListNode(1)
head.next.next=ListNode(2)
head.next.next.next=ListNode(3)
head.next.next.next.next=ListNode(3)
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