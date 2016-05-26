class Solution(object):            #BS, time o(nlogn)
    def findDuplicate(self, nums): #requirement is o(1) extra space
        """
        :type nums: List[int]
        :rtype: int
        """
        l,h = 1,len(nums)-1
        while l<=h:
          m=(l+h)/2
          cnt=sum(x<=m for x in nums)
          if cnt>m: h=m-1
          else: l=m+1
        return l