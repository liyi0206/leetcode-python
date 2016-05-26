class Solution(object):
    def threeSumSmaller(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        if not nums: return 0
        nums.sort()
        res=0
        for i,num in enumerate(nums[:-2]):
            j,k=i+1,len(nums)-1
            while j<k:
                #print "idx",i,j,k,"nums",nums[i],nums[j],nums[k]
                if nums[j]+nums[k]+num<target: 
                    res+=k-j
                    j=j+1 #every time only change one pointer, or may miss elem
                else: k-=1 
        return res
        
a=Solution()
#print a.threeSumSmaller([-1,2,1,-4],1) #2
print a.threeSumSmaller([3,1,0,-2],4) #3