class Solution(object):
    def lengthOfLongestSubstringKDistinct(self, s, k):
        """
        :type s: str
        :type k: int
        :rtype: int
        """
        mp={}
        res=0
        p1,p2=0,0
        while p2<len(s):
            #print p1,p2,mp
            if s[p2] not in mp: mp[s[p2]]=1
            else: mp[s[p2]]+=1
            if len(mp)==k+1:
                res=max(res,p2-p1)
                while len(mp)>k:
                    #print "inner",p1,p2,mp
                    mp[s[p1]]-=1
                    if mp[s[p1]]==0: mp.pop(s[p1])
                    p1+=1
            p2+=1
        res=max(res,p2-p1)
        return res
        
a=Solution()
print a.lengthOfLongestSubstringKDistinct('eceba',2) #3
print a.lengthOfLongestSubstringKDistinct('eceba',3) #4