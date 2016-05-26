class Solution(object):
    def threeSumClosest(self,nums,target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        nums.sort()
        diff,res=100000000,-1
        for i,num in enumerate(nums):
            j,k=i+1,len(nums)-1
            while j<k:
                tmp=nums[j]+nums[k]+num-target
                if abs(tmp)<diff: 
                    res=nums[j]+nums[k]+num
                    diff=abs(tmp)
                if tmp==0: return target
                elif tmp>0: k-=1
                else: j+=1
        return res
        
    def threeSumClosest2(self,nums,target):
        nums.sort()
        res=None
        for i,num in enumerate(nums[:-2]):
            j,k=i+1,len(nums)-1
            while j<k:
                tmp=nums[j]+nums[k]+num-target
                ##Don't use not res - when res==0, not res also True
                if res==None or abs(tmp)<abs(res-target): 
                    res=nums[j]+nums[k]+num
                if tmp==0: return res
                elif tmp>0: k-=1
                else: j+=1
        return res
        
a=Solution()
print a.threeSumClosest2([-1,2,1,-4],1) #2
print a.threeSumClosest2([0,2,1,-3],1) #0