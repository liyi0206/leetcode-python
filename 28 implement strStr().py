class Solution(object):
    def strStr(self, haystack, needle):
        """
        :type haystack: str
        :type needle: str
        :rtype: int
        """
        m = len(needle)
        for i in range(len(haystack)-m+1):
            if haystack[i:i+m] == needle:
                return i
        return -1

    def strStr2(self, haystack, needle):
        lenh, lenn = len(haystack), len(needle)
        if lenn == 0: return haystack
        next, p = [-1] * (lenn), -1
        for i in range(1, lenn):
            print i
            while p>=0 and needle[i]!=needle[p+1]: p = next[p]
            if needle[i] == needle[p+1]: p=p+1
            next[i] = p
        print "next",next
        p = -1
        for i in range(lenh):
            while p >= 0 and haystack[i] != needle[p+1]: p=next[p]
            if haystack[i] == needle[p+1]: p=p+1
            if p + 1 == lenn: return i-p
        return -1
            
a=Solution()
print a.strStr2("somegibberishhello","hello")