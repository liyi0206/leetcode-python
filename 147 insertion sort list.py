# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution(object):
    def insertionSortList(self, head): #TLE
        """
        :type head: ListNode
        :rtype: ListNode
        """
        if head is None: return None
        dummy=ListNode(0)
        pre,cur=dummy,head
        while cur:
            nxt=cur.next
            pre=dummy
            while pre.next and pre.next.val<cur.val:
                pre=pre.next
            cur.next=pre.next
            pre.next=cur
            cur=nxt
        return dummy.next
        
    def insertionSortList2(self,head): #AC
        if head is None or head.next is None: return head
        dummy = ListNode(0)
        dummy.next = head
        cur = head
        while cur.next:
            if cur.next.val < cur.val:
                pre = dummy
                while pre.next.val < cur.next.val:
                    pre = pre.next
                temp = cur.next
                cur.next = temp.next
                temp.next = pre.next # put temp after pre
                pre.next = temp
            else:
                cur = cur.next
        return dummy.next
 
        
node1,node2,node3 = ListNode(3),ListNode(1),ListNode(2)
nodes = [node1,node2,node3]
for i in range(len(nodes)-1):
    nodes[i].next = nodes[i+1]

cur = node1
while cur: print cur.val,;cur=cur.next
print

a=Solution()
new=a.insertionSortList2(node1)
cur = new
while cur: print cur.val,;cur=cur.next