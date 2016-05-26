class Solution(object):
    def lengthOfLongestSubstringTwoDistinct(self, s):
        """
        :type s: str
        :rtype: int
        """
        mp={}
        res=0
        p1,p2=0,0
        while p2<len(s):
            #print p1,p2,mp
            if s[p2] not in mp: mp[s[p2]]=1
            else: mp[s[p2]]+=1
            if len(mp)==3:
                res=max(res,p2-p1)
                while len(mp)>2:
                    #print "inner",p1,p2,mp
                    mp[s[p1]]-=1
                    if mp[s[p1]]==0: mp.pop(s[p1])
                    p1+=1
            p2+=1
        res=max(res,p2-p1)
        return res
        
a=Solution()
print a.lengthOfLongestSubstringTwoDistinct('eceba') #3
print a.lengthOfLongestSubstringTwoDistinct("abcabcabc") #2
print a.lengthOfLongestSubstringTwoDistinct("a") #1

# remember to p1+=1 after s[p1] checks
# remember to p2+=1 for all cases, no matter p1 moves or not
# same as #3, different with #76, update res before moving p1
# same as #3, different with #76, update res at last too