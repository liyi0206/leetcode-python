class Solution(object):
    def findMinHeightTrees(self, n, edges):
        """
        :type n: int
        :type edges: List[List[int]]
        :rtype: List[int]
        """
        #a tree is an undirected graph in which any two vertices are connected by exactly one path.
        #any parent could have >2 children
        # How many MHTs can a graph have at most? 2
        if not edges: return []
        neighbors=[set() for x in range(n)]
        for n1,n2 in edges:
            neighbors[n1].add(n2)
            neighbors[n2].add(n1)
        
        # BFS, start from leaves
        leaves=[x for x in range(n) if len(neighbors[x])<=1] #<1 only for single point case
        while n>2: #stop rule is n, not leaves, as the final leaves is res, with 1 or 2 entries
            n-=len(leaves)
            nxt=[]
            for x in leaves:
                for y in neighbors[x]:
                    neighbors[y].remove(x)
                    if len(neighbors[y])==1: nxt.append(y)
            leaves=nxt
        return leaves
        
a=Solution()
print a.findMinHeightTrees(n=4, edges=[[1,0],[1,2],[1,3]]) #1
print a.findMinHeightTrees(n=6, edges=[[0,3],[1,3],[2,3],[4,3],[5,4]]) #[3,4]