class Solution(object):
    def findMissingRanges(self, nums, lower, upper):
        """
        :type nums: List[int]
        :type lower: int
        :type upper: int
        :rtype: List[str]
        """
        #1, when nums[i]>p, go directly to p=nums[i]
        #   cur=old p, and compare with new p
        #2, if not nums or nums[-1]<p
        res=[]
        i=0
        p=lower
        cur=None
        while i<len(nums) and p<upper:
            if nums[i]==p:
                p+=1
                i+=1
            elif nums[i]>p: 
                cur=p
                p=nums[i] #p++
                if cur<p-1: res.append(str(cur)+"->"+str(p-1))
                else: res.append(str(cur))  
            else: i+=1
        if not nums or nums[-1]<p:
            if p<upper: res.append(str(p)+"->"+str(upper))
            else: res.append(str(p))
        return res
        
    def findMissingRanges2(self, nums, lower, upper):
        p = lower
        res = []
        nums.append(upper+1)
        for cur in nums:
            if cur==p+1: res.append(str(p))
            elif cur>p+1: res.append(str(p)+"->"+str(cur-1))
            p = cur+1
        return res


a=Solution()
print a.findMissingRanges([0,1,3,50,75],0,99) #["2","4->49","51->74","76->99"]
print a.findMissingRanges([-1000000000,-9999,0,1,2,10,100,1000,999999999,1000000000],-1000000000,1000000000)
print a.findMissingRanges([],1,1) #1