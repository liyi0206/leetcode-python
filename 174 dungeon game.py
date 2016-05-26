class Solution(object):
    def calculateMinimumHP(self, dungeon):
        """
        :type dungeon: List[List[int]]
        :rtype: int
        """
        w,h = len(dungeon[0]),len(dungeon)
        hp = [[0]*w for i in range(h)]
        hp[h-1][w-1] = max(1-dungeon[h-1][w-1],1)
        for i in range(h-1,-1,-1):
            for j in range(w-1,-1,-1):
                down,right = None,None
                if i+1<h: down =max(hp[i+1][j]-dungeon[i][j],1)
                if j+1<w: right=max(hp[i][j+1]-dungeon[i][j],1)
                if down and right: hp[i][j]=min(down,right)
                elif down: hp[i][j]=down
                elif right:hp[i][j]=right
        return hp[0][0]
        
dungeon=[[-2,-3,3],[-5,-10,1],[10,30,-5]]
a=Solution()
print a.calculateMinimumHP(dungeon)