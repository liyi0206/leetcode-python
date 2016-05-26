class Solution(object):
    def searchMatrix(self, matrix, target):
        """
        :type matrix: List[List[int]]
        :type target: int
        :rtype: bool
        """ 
        if not matrix: return 0
        curRow,curCol=0,len(matrix[0])-1
        while curRow<len(matrix) and curCol>=0:
            if matrix[curRow][curCol]==target:return True
            elif matrix[curRow][curCol]>target: curCol-=1
            else: curRow+=1
        return False
        
    #def searchMatrix(self, matrix, target):
    #    self.matrix=matrix
    #    self.target=target
    #    if not matrix or not matrix[0]:
    #        return False
    #    return self.helper(0,len(matrix)-1,0,len(matrix[0])-1)
    #    
    #def helper(self,rl,rh,cl,ch):
    #    if rl >rh or cl>ch: return False
    #    if rl==rh and cl==ch: return self.matrix[rl][cl]==self.target
    #    rm,cm=(rl+rh)/2,(cl+ch)/2
    #    v=self.matrix[rm][cm]
    #    if v==self.target: return True
    #    elif v>self.target: return self.helper(rl,rm-1,cl,ch) or self.helper(rm,rh,cl,cm-1)
    #    else: return self.helper(rm+1,rh,cl,ch) or self.helper(rl,rm,cm+1,ch)
        
