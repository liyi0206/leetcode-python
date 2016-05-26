class Solution(object):
    def countPrimes(self, n): # Sieve of Eratosthenes
        """
        :type n: int
        :rtype: int
        """
        # to find all primes under n, get all primes under sqrt(n), keep the
        # prime and remove all its multiples. Whatever leftover are primes.
        
        # why primes under sqrt(n), then the smallest valid multiple of it will 
        # be p**2, o/2 any number=p*i where i<p is already covered previously.
        
        if n<=2: return 0
        mp = range(n)
        mp[1]=0
        i=2
        while (i*i<n):
            if mp[i]!=0:
                j=2
                while j*i<n: 
                    mp[j*i]=0
                    j+=1
            i+=1
        #print mp
        return sum([1 for a in mp if a>0])
        
a=Solution()
print a.countPrimes(3)