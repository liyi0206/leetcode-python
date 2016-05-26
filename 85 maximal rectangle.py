class Solution:
    def maximalRectangle(self, matrix):
        heights = [[0]*len(matrix[0]) for i in range(len(matrix))]
        for i in range(len(matrix)):
            for j in range(len(matrix[0])):
                if matrix[i][j] == "0": heights[i][j] = 0
                elif i == 0: heights[i][j] = 1
                else: heights[i][j] = int(heights[i-1][j]) + 1
        res=0
        for i in range(len(matrix)):
            res=max(res,self.largestRectangleArea(heights[i]))
        return res
        
    # This is the solution for question Largest Rectangle in Histogram
    def largestRectangleArea(self, heights):
        if len(heights)==0: return 0
        res=0
        heights.append(0)
        stack=[]
        for i in range(len(heights)):
            while stack and heights[stack[-1]]>heights[i]:
                tmp=stack.pop()
                if not stack: w=i
                else: w=i-1-stack[-1]
                res=max(res, w*heights[tmp])
            stack.append(i)
            #print i,stack
        return res
    
matrix=[["0","0","1"],
        ["0","0","1"],
        ["0","0","1"]]
a=Solution()
print a.maximalRectangle(matrix)