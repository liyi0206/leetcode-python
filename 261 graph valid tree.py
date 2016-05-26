class Solution(object):
    def validTree(self, n, edges): #union find
        """
        :type n: int
        :type edges: List[List[int]]
        :rtype: bool
        """
        #any connected graph without simple cycles is a tree
        #any parent could have >2 children
        roots=range(n)
        for n1,n2 in edges:
            x=self.find(roots,n1)
            y=self.find(roots,n2)
            if x==y: return False # no cycle
            roots[x]=y #union
        return len(edges)==n-1 #each node connects itself once **
        
    def find(self,roots,id):
        while roots[id]!=id:
            roots[id]=roots[roots[id]]
            id=roots[id]
        return id

a=Solution()
print a.validTree(5,[[0, 1], [0, 2], [0, 3], [1, 4]]) #True
print a.validTree(5,[[0, 1], [1, 2], [2, 3], [1, 3], [1, 4]]) #False