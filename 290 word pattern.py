class Solution(object):
    def wordPattern(self, pattern, str):
        """
        :type pattern: str
        :type str: str
        :rtype: bool
        """
        map1,map2 = dict(),dict()
        for i in range(len(pattern)):
            if pattern[i] not in map1: map1[pattern[i]]=[i]
            else: map1[pattern[i]].append(i)
        string = str.split()
        for i in range(len(string)):
            if string[i] not in map2: map2[string[i]]=[i]
            else: map2[string[i]].append(i)
            
        set1,set2 = set(),set()
        for k,v in map1.iteritems(): set1.add(tuple(v))
        for k,v in map2.iteritems(): set2.add(tuple(v))
        return set1==set2
            
a = Solution()
print a.wordPattern(pattern = "abba", str = "dog cat cat dog")
print a.wordPattern(pattern = "abba", str = "dog cat cat fish")
print a.wordPattern(pattern = "aaaa", str = "dog cat cat dog")
print a.wordPattern(pattern = "abba", str = "dog dog dog dog")