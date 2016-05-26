class Solution(object):
    def maxSlidingWindow(self, nums, k): #naive, o(nk)
        """
        :type nums: List[int]
        :type k: int
        :rtype: List[int]
        """
        res=[]
        for i in range(len(nums)-k+1):
            res.append(max(nums[i:i+k]))
        return res
        
    def maxSlidingWindow2(self,nums,k): #deque stack o(n), extra space o(k)
        dq = [] #should be collections.deque(), so pop(0) is o(1)
        res = []
        for i in range(len(nums)):
            # remove all the smaller numbers, as they are not useful any more
            # if remove from head is slower than remove from end
            while dq and nums[dq[-1]]<=nums[i]: dq.pop()
            dq.append(i)
            if dq[0]==i-k: dq.pop(0)
            if i>=k-1: res.append(nums[dq[0]])
        return res 
        
a=Solution()
print a.maxSlidingWindow2([1,3,-1,-3,5,3,6,7],3) #[3,3,5,5,6,7]