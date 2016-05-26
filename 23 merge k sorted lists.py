# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution(object):
    def mergeKLists(self, lists):
        """
        :type lists: List[ListNode]
        :rtype: ListNode
        """
        import heapq
        dummy = ListNode(0)
        current = dummy
        heap = []
        for sorted_list in lists:
            if sorted_list:
                heapq.heappush(heap, (sorted_list.val, sorted_list))
        while heap:
            smallest = heapq.heappop(heap)[1]
            current.next = smallest
            current = current.next
            if smallest.next:
                heapq.heappush(heap, (smallest.next.val, smallest.next))
        return dummy.next
        
l1=ListNode(1)
l1.next=ListNode(3)
l1.next.next=ListNode(5)
l1.next.next.next=ListNode(7)

l2=ListNode(2)
l2.next=ListNode(8)
l2.next.next=ListNode(9)

l3=ListNode(4)
l3.next=ListNode(6)
l3.next.next=ListNode(10)

a=Solution()
l=a.mergeKLists([l1,l2,l3])
cur = l
while cur:
    print cur.val,
    cur=cur.next