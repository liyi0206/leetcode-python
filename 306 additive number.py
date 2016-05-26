class Solution(object):
    def isAdditiveNumber(self, num):
        """
        :type num: str
        :rtype: bool
        """
        import itertools
        n = len(num)
        for i, j in itertools.combinations(range(1, n*2/3+1), 2):
            #print (i,j)
            a, b = num[:i], num[i:j]
            if (a!='0' and a[0]=='0') or (b!='0' and b[0]=='0'): continue
            while j < n:
                c = str(int(a)+int(b))
                if not c==num[j:j+len(c)]: break
                j += len(c)
                a, b = b, c
                #print (a,b)
            if j == n: return True
        return False
        
a=Solution()
#print a.isAdditiveNumber("112358")
#print a.isAdditiveNumber("199100199")
#print a.isAdditiveNumber("123")
print a.isAdditiveNumber("0235813")