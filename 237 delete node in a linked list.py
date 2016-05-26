# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution(object):
    def deleteNode(self, node):
        """
        :type node: ListNode
        :rtype: void Do not return anything, modify node in-place instead.
        """
        node.val = node.next.val
        node.next = node.next.next
        
node1,node2,node3,node4 = ListNode(1),ListNode(2),ListNode(3),ListNode(4)
nodes = [node1,node2,node3,node4]
for i in range(len(nodes)-1):
    nodes[i].next = nodes[i+1]

cur = node1
while cur:
    print cur.val,
    cur=cur.next
print

a=Solution()
a.deleteNode(node3)
cur = node1
while cur:
    print cur.val,
    cur=cur.next
        