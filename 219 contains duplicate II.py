class Solution(object):
    def containsNearbyDuplicate(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: bool
        """
        map = dict()
        for i in range(len(nums)):
            if nums[i] not in map: map[nums[i]]=[i]
            else: 
                map[nums[i]].append(i)
                for j in range(len(map[nums[i]])-1):
                    if map[nums[i]][j+1]-map[nums[i]][j]<=k:
                        return True
        return False
        
a=Solution()
print a.containsNearbyDuplicate([-1,-1],1)
print a.containsNearbyDuplicate([1,2,1,3,4,5,6,7,8,9],3)
print a.containsNearbyDuplicate([1,2,3,4,5,6,7,1,8,9],3)