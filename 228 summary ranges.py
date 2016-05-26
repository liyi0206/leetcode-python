class Solution(object):
    def summaryRanges(self, nums):
        """
        :type nums: List[int]
        :rtype: List[str]
        """
        if not nums: return []
        res=[]
        i,tmp =0,str(nums[0])
        nums.append(nums[-1]+2)
        while i+1<len(nums):
            if nums[i+1] != nums[i]+1: 
                if str(nums[i])!= tmp:
                    tmp=tmp+"->"+str(nums[i])
                #print tmp
                res.append(tmp)
                tmp=str(nums[i+1])
            i+=1
        return res
        
    # 1, nums append a larger number to avoid loop overflow
    # 2, if cur==nums[i], only str(cur) is enough
    def summaryRanges2(self, nums): #tried again
        if not nums: return []
        res=[]
        #i=0
        cur=nums[0]
        nums.append(nums[-1]+2) #
        #while i<len(nums)-1:
        for i in range(len(nums)-1):
            if nums[i+1]!=nums[i]+1:
                if cur<nums[i]:
                    res.append(str(cur)+"->"+str(nums[i]))
                else: res.append(str(cur))
                cur=nums[i+1]
            #i+=1
        return res
        
a=Solution()
print a.summaryRanges([0,1,2,4,5,7]) #["0->2","4->5","7"]
print a.summaryRanges([0,1,2,4,5,6])
print a.summaryRanges([0,1,2,4,6,7])
print a.summaryRanges([0])
print a.summaryRanges([])
print a.summaryRanges([-1])