class Solution(object):
    def groupStrings(self, strings):
        """
        :type strings: List[str]
        :rtype: List[List[str]]
        """
        mp={}
        for s in strings:
            #%26 is the key point - so 'zab' will return (0,1,2)
            key=tuple((ord(c)-ord(s[0]))%26 for c in s) 
            if key not in mp: mp[key]=[s]
            else: mp[key].append(s)
        return [sorted(a) for a in mp.values()]
            
a=Solution()
print a.groupStrings(["abc","bcd","acef","xyz","az","ba","a","z"]) #4 groups