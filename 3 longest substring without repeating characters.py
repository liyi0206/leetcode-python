class Solution(object):
    def lengthOfLongestSubstring(self, s):
        """
        :type s: str
        :rtype: int
        """
        p1,p2,res,dict=0,0,0,{} #dict to keep letter:idx pairs
        while p2<len(s):
            if s[p2] not in dict:
                dict[s[p2]] = p2
                p2 += 1
                res = max(res,p2-p1)
            else:
                p = dict[s[p2]]
                while p1<=p:
                    dict.pop(s[p1])
                    p1 +=1
        return res
        
    def lengthOfLongestSubstring2(self,s):
        p1,p2=0,0
        res=0
        visited=set()
        while p2<len(s): 
            if s[p2] in visited: 
                res=max(res,p2-p1)
                while s[p2] in visited:
                    visited.remove(s[p1])
                    p1+=1
            visited.add(s[p2])
            p2+=1
        res=max(res,p2-p1)
        return res
        
a=Solution()
print a.lengthOfLongestSubstring("abcabcbb")
print a.lengthOfLongestSubstring("bbbbb")