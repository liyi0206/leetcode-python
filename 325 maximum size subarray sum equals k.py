class Solution(object):
    def maxSubArrayLen(self, nums, k): #O(n) time
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """
        if not nums: return 0
        sums=[nums[0]]
        for n in nums[1:]: sums.append(sums[-1]+n)
        res=0
        #mp={sums[0]:0}
        mp={}
        for j in range(len(sums)):
            if sums[j]==k: res=max(res,j+1)
            elif sums[j]-k in mp:   # s-sums[i]=k
                i=mp[sums[j]-k]     # s-k=sums[i]
                res=max(res,j-i)
            if sums[j] not in mp: mp[sums[j]]=j
        return res
        
    def maxSubArrayLen2(self, nums, k): #O(n) time - optimized for mp
        if not nums: return 0
        sums=[nums[0]]
        for n in nums[1:]: sums.append(sums[-1]+n)
        res=0
        mp={0:-1}
        for j in range(len(sums)):
            if sums[j]-k in mp:   # s-sums[i]=k
                i=mp[sums[j]-k]   # s-k=sums[i]
                res=max(res,j-i)
            if sums[j] not in mp: mp[sums[j]]=j
        return res
        
a=Solution()
print a.maxSubArrayLen([1,-1,5,-2,3],3) #4
print a.maxSubArrayLen([-2,-1,2,1],1) #2