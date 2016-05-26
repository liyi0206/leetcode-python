import heapq
class Solution(object):
    #def nthSuperUglyNumber(self, n, primes):
    #    """
    #    :type n: int
    #    :type primes: List[int]
    #    :rtype: int
    #    """
    #    res = [1]
    #    idx=[0]*len(primes)
    #    while len(res)<n:
    #        h=[]
    #        for i in range(len(idx)):
    #            heapq.heappush(h,primes[i]*res[idx[i]])
    #        m=heapq.heappop(h)
    #        for i in range(len(idx)):
    #            if m == primes[i]*res[idx[i]]: idx[i]+=1
    #        res += [m]
    #        #print indices,q
    #    return res[-1]
        
    def nthSuperUglyNumber(self, n, primes):
        res = [1]
        idx = [0]*len(primes)
        h = [(primes[i]*res[idx[i]], i) for i in xrange(len(idx))] 
        heapq.heapify(h)
        while len(res) < n:
            (m, min_idx) = heapq.heappop(h)
            idx[min_idx]+= 1               # idx +1
            if m != res[-1]: res.append(m) # res append
            heapq.heappush(h, (primes[min_idx]*res[idx[min_idx]], min_idx))
        return res[-1]
        
a=Solution()
print a.nthSuperUglyNumber(12,[2,7,13,19]) #32
print a.nthSuperUglyNumber(100000,[7,19,29,37,41,47,53,59,61,79,83,89,101,103,\
    109,127,131,137,139,157,167,179,181,199,211,229,233,239,241,251]) #1092889481
