class Solution(object):
    def majorityElement(self, nums):# o(1) space and o(n) time
                                    # if exist, must be in the mp
                                    # but might not exist, so need double check.
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        mp={}
        for n in nums:
            if n in mp: mp[n]+=1
            elif len(mp)<2: mp[n]=1
            else:
                keys=[k for k in mp]
                for k in keys:
                    mp[k]-=1
                    if mp[k]==0: mp.pop(k)
            #print mp
        res=[]
        mp={k:0 for k in mp}
        for n in nums:
            if n in mp:
                mp[n]+=1
        #print "new mp",mp
        res=[k for k in mp if mp[k]>len(nums)/3]
        return res
        
a=Solution()
print a.majorityElement([1,2,3,1,4,3,1,1])