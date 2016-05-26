# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution(object):
    def isPalindrome(self, head):
        """
        :type head: ListNode
        :rtype: bool
        """
        if not head: return None
        
        # find the mid node
        p1,p2=head,head
        while p2.next and p2.next.next:
            p1=p1.next
            p2=p2.next.next
        #print p1.val,p2.val
            
        # reverse the second half
        prev=None
        cur=p1.next #head of the second half
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
        
        # compare the first and second half nodes
        p1,p2=head,prev
        while p2: # while node and head:
            if p2.val!= p1.val: return False
            p2 = p2.next
            p1 = p1.next
        return True

root=ListNode(1)
cur=root
for i in range(2,9): #try odd and even numbers
    cur.next=ListNode(i)
    cur=cur.next
a=Solution()
print a.isPalindrome(root)