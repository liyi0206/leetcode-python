class Solution(object):
    def maxCoins(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        n=len(nums)  
        self.nums=[1]+nums+[1]  
        self.dp=[[0 for j in range(n+2)] for i in range(n+2)]
        return self.dfs(1,n) #i,j means only have i-j balloons

    def dfs(self,i,j):
        if self.dp[i][j]>0: return self.dp[i][j]
        for x in range(i,j+1): #x is the last burst balloon
            self.dp[i][j]=max(self.dp[i][j], self.dfs(i,x-1)+self.dfs(x+1,j)+ \
                                             self.nums[i-1]*self.nums[x]*self.nums[j+1])  
        return self.dp[i][j]
        
    def maxCoins2(self,nums):
        nums = [1]+[i for i in nums if i>0]+[1]
        n = len(nums)
        dp = [[0]*n for i in xrange(n)]
    
        for k in xrange(2,n): #2,n-1
            for left in xrange(0,n-k):
                right = left+k 
                #print left,right
                # left/right are the dummies, outside of all burst balloons
                for i in xrange(left+1,right): #i is the last burst balloon
                    dp[left][right] = max(dp[left][right],
                        #last balloon at i, with neighbors left and right
                        dp[left][i]+nums[left]*nums[i]*nums[right]+dp[i][right])    
        return dp[0][n-1]
        
a=Solution()
print a.maxCoins2([3,1,5,8]) #167