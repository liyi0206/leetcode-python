class Solution(object):
    def minSubArrayLen(self, s, nums):
        """
        :type s: int
        :type nums: List[int]
        :rtype: int
        """
        p1,p2,res = 0,0,0
        while p2<len(nums):
            if sum(nums[p1:p2+1])<s: p2=p2+1
            else:
                while sum(nums[p1:p2+1])>=s: p1=p1+1
                if res==0 or (p2+1)-(p1-1)<res: res=(p2+1)-(p1-1)
        return res

a=Solution()
print a.minSubArrayLen(7,[2,3,1,2,4,3])