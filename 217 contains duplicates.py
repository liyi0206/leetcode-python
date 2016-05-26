class Solution(object):
    def containsDuplicate(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        set1=set()
        for n in nums:
            if n not in set1: set1.add(n)
            else: return True
        return False
        
a = Solution()
print a.containsDuplicate([1,2,3,4,5,6,7,1,8,9])