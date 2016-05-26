# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution(object): # iter
    def reverseList(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        if not head: return None
        dummy=ListNode(0)
        dummy.next=head
        
        cur=dummy
        front=None
        while cur.next:  
            tmp=cur.next
            cur.next=cur.next.next 
            tmp.next=front
            front=tmp
        return front
        
    def reverseList1(self, head): # without dummy
        if not head: return None
        prev=head
        cur=head.next
        head.next=None #can't remove, o/w 1,2,1,2,1,2,1,2...
        while cur:
            tmp=cur.next
            cur.next=prev
            prev=cur
            cur=tmp
        return prev
    
    def reverseList2(self, head): # with one less operation in loop ***
        if not head: return None
        prev=None
        cur=head
        while cur:
            tmp=cur.next
            cur.next=prev
            #head.next=tmp
            prev=cur
            cur=tmp
        return prev
            
class Solution2(object): # recur *********very important*********
    def reverseList(self,head):
        return self.recur(head,None)
        
    def recur(self,cur,new): #old_list, new_list
        if not cur: return new
        tmp=cur.next
        cur.next=new
        return self.recur(tmp,cur)

        
head=ListNode(1)
head.next=ListNode(2)
head.next.next=ListNode(3)
head.next.next.next=ListNode(4)
cur = head
while cur:
    print cur.val,
    cur=cur.next
print

a=Solution()
new=a.reverseList1(head)
cur = new
while cur:
    print cur.val,
    cur=cur.next