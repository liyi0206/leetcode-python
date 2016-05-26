class Solution(object):
    def majorityElement(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        map1={}
        for n in nums:
            if n not in map1: map1[n]=1
            else: map1[n] += 1
            if map1[n]>len(nums)/2: return n
        return None
        
a = Solution()
print a.majorityElement([1,2,2,1,1,1,1,3,4])