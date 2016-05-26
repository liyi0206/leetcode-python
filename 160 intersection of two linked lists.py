# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None
        
# no cycle
# o(n) time, o(1) space, do not change input

class Solution(object):
    def getIntersectionNode(self, headA, headB):
        """
        :type head1, head1: ListNode
        :rtype: ListNode
        """
        len1,len2=0,0
        cur=headA
        while cur:
            cur=cur.next
            len1+=1
        cur=headB
        while cur:
            cur=cur.next
            len2+=1
        
        while len1>len2:
            headA=headA.next
            len1-=1
        while len1<len2:
            headB=headB.next
            len2-=1
        while headA!=headB:
            headA=headA.next
            headB=headB.next
        return headA