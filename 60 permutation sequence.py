class Solution(object):
    def getPermutation(self, n, k):
        """
        :type n: int
        :type k: int
        :rtype: str
        """
        import math
        seq, k, fact = "", k - 1, math.factorial(n - 1)
        perm = [i for i in range(1, n + 1)]
        #print perm
        for i in reversed(range(n)):
            curr = perm[k / fact]
            #print k,fact,k/fact,curr
            seq += str(curr)
            perm.remove(curr)
            if i > 0:
                #print "k,fact,k=k%fact:",k,fact,k%fact
                k %= fact
                #print "fact,i,fact=fact/i:",fact,i,fact/i,"\n"
                fact /= i
        return seq
        
a=Solution()
print a.getPermutation(3,5)