class Solution(object):
    def wallsAndGates(self, rooms):
        """
        :type rooms: List[List[int]]
        :rtype: void Do not return anything, modify rooms in-place instead.
        """
        if not rooms: return None
        n,m=len(rooms),len(rooms[0])
        cur=[(i,j) for i in range(n) for j in range(m) if rooms[i][j]==0]
        k=0
        while cur:
            k+=1
            nxt=[]
            for (i,j) in cur:
                for x,y in ((i+1,j),(i-1,j),(i,j+1),(i,j-1)):
                    if 0<=x<n and 0<=y<m and rooms[x][y]==-2:
                        rooms[x][y]=k
                        nxt.append((x,y))
            cur=nxt

#import sys
#INF=sys.maxint
rooms=[ [-2,-1,0,-2],
        [-2,-2,-2,-1],
        [-2,-1,-2,-1],
        [0,-1,-2,-2]]
a=Solution()
a.wallsAndGates(rooms)
for l in rooms: print l