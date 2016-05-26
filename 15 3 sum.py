class Solution(object):
    def threeSum(self, A):
        """
        :type A: List[int]
        :rtype: List[List[int]]
        """
        A,res,i = sorted(A),[],0
        while i < len(A)-2:
            j,k = i+1, len(A)-1
            while j < k:
                if A[i]+A[j]+A[k] < 0: j += 1
                elif A[i]+A[j]+A[k] > 0: k -= 1
                else:
                    res.append([A[i],A[j],A[k]])
                    j,k = j+1,k-1
                    while j<k and A[j]==A[j-1]: j+=1
                    while j<k and A[k]==A[k+1]: k-=1
            i += 1
            while i <len(A)-2 and A[i]==A[i-1]: i+=1
        return res
        
a=Solution()
print a.threeSum([-1,0,1,2,-1,-4])