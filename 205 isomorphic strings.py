class Solution(object):
    def isIsomorphic(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: bool
        """
        map1={}
        for i in range(len(s)):
            if s[i] not in map1: map1[s[i]]=[i]
            else: map1[s[i]].append(i)
        set1=set([tuple(v) for k,v in map1.iteritems()])
        print set1
        
        map2={}
        for i in range(len(t)):
            if t[i] not in map2: map2[t[i]]=[i]
            else: map2[t[i]].append(i)
        set2=set([tuple(v) for k,v in map2.iteritems()])
        print set2
        
        return set1==set2
        
a = Solution()
print a.isIsomorphic("egg", "add")
print a.isIsomorphic("foo", "bar")
print a.isIsomorphic("paper", "title")