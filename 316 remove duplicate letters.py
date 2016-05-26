class Solution(object):
    def removeDuplicateLetters2(self, s):
        """
        :type s: str
        :rtype: str
        """
        import collections
        mp = collections.Counter(s)
        st = set() #keep the set for o(1) search
        stack = list()
        for c in s:
            #1 update mp, whatever
            mp[c]-=1 
            #2 if already used, means used before larger ones, skip
            if c in st: continue 
            #3 pop prev only when larger and still available
            while stack and stack[-1]>c and mp[stack[-1]]:
                st.remove(stack.pop())
            #4 push to stack and st
            stack.append(c)
            st.add(c)
        return ''.join(stack)

a=Solution()
print a.removeDuplicateLetters1("bcabc") #abc
print a.removeDuplicateLetters1("cbacdcbc") #acdb
print a.removeDuplicateLetters1("bbcaac") #bac