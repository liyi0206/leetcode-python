# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution(object):
    def sortList(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        return self.mergeSort(head)
        
    def mergeSort(self,head):
        if head is None or head.next is None: return head
        walker,runner=head,head
        while runner.next and runner.next.next:
            walker=walker.next
            runner=runner.next.next
        head1,head2=head,walker.next
        walker.next=None
        head1,head2=self.mergeSort(head1),self.mergeSort(head2)
        return self.merge(head1,head2)
        
    def merge(self,head1,head2):
        dummy=ListNode(0)
        dummy.next=head1
        pre=dummy
        while head1 and head2:
            if head1.val<head2.val: head1=head1.next
            else:
                nxt=head2.next
                head2.next=pre.next #put head2 after pre
                pre.next=head2
                head2=nxt
            pre=pre.next
        if head2: pre.next=head2
        return dummy.next
        
node1,node2,node3 = ListNode(3),ListNode(1),ListNode(2)
nodes = [node1,node2,node3]
for i in range(len(nodes)-1):
    nodes[i].next = nodes[i+1]

cur = node1
while cur: print cur.val,;cur=cur.next
print

a=Solution()
new=a.sortList(node1)
cur = new
while cur: print cur.val,;cur=cur.next