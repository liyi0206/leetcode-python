class Solution(object):
    # There is a fence with n posts, 
    # each post can be painted with one of k colors. 
    # no more than two adjacent fence posts have the same color.
    # Return the total number of ways you can paint the fence.
    
    def numWays(self,n,k):
        if n==0: return 0
        elif n==1: return k
        elif n==2: return k*k
        
        pp,p = k,k*k
        for n in range(2,n):
            # use dp to avoid considering p and pp color combinations
            # we couldn't separate their combinations, too many cases
            # so consider only cur and p, using p and pp final status
            
            # pp*(k-1) cur and p same color, so pp and they are different
            # p*(k-1)  cur and p different colors, no matter p what color
            cur = pp*(k-1)+p*(k-1)
            pp,p = p,cur
        return cur
        
# example, k=3, dp[0]=3,dp[1]=3*3=9, if no restriction, dp[2]=3^3=27
# but with restriction, dp[2]=3*2+9*2=24, without the three same color case.
        
a=Solution()
print a.numWays()