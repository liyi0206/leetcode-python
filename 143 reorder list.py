# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution(object):
    def reorderList(self, head):
        """
        :type head: ListNode
        :rtype: void Do not return anything, modify head in-place instead.
        """
        if not head or not head.next: return
        
        # Find the middle of the list - p1
        p1,p2=head,head
        while p2.next and p2.next.next:
            p1=p1.next
            p2=p2.next.next 
            
        # reverse the half after middle
        # 1->2->3->4->5->6 to 1->2->3->6->5->4
        prev=None
        cur=p1.next #head of the second half, no matter odd or even number
        while cur:
            tmp=cur.next
            cur.next=prev
            prev=cur
            cur=tmp
        p1.next=prev

        #pp=head
        #while pp:
        #    print pp.val,
        #    pp=pp.next

        # start reorder one by one
        # 1->2->3->6->5->4 to 1->6->2->5->3->4
        half_end=p1
        p1,p2=head,half_end.next
        while p1!=half_end:
            half_end.next=p2.next
            p2.next=p1.next
            p1.next=p2
            p1=p2.next
            p2=half_end.next
        
        #pp=head
        #while pp:
        #    print pp.val,
        #    pp=pp.next

root=ListNode(1)
cur=root
for i in range(2,9): #try odd and even numbers
    cur.next=ListNode(i)
    cur=cur.next
a=Solution()
a.reorderList(root)
