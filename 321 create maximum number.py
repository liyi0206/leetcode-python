class Solution(object):
    def maxNumber(self, nums1, nums2, k):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :type k: int
        :rtype: List[int]
        """
        def getMax(nums, t):
            stack = []
            size = len(nums)
            for x in range(size):
                # pop if: stack end smaller than new number, and
                # elem in array enough to make stack enough length
                while stack and len(stack)+size-x>t and stack[-1]<nums[x]: 
                    stack.pop()
                # 1 condition for append - stack length not enough
                if len(stack)<t: stack.append(nums[x])
            return stack

        def merge(nums1, nums2):
            res = [] 
            while nums1 or nums2:
                # use array comparison (with pop), but not elem comparison 
                # by two pointers, because -
                # 1, in case of [6,7], [6,0,4], 5, second elem counts.
                # 2, easier for dealing one side residual, as [3]>[] is True.
                if nums1>nums2: res.append(nums1.pop(0))
                else: res.append(nums2.pop(0))
            return res
        
        len1, len2 = len(nums1), len(nums2)
        res = []
        # k<=len1+len2 (not used)
        # 0<=x<=len1 (*)
        # 0<=k-x<len2 => k-len2<=x<=k (*)
        for x in range(max(0,k-len2),min(k,len1)+1):
            tmp = merge(getMax(nums1,x), getMax(nums2,k-x))
            res = max(tmp,res)
        return res
        
a=Solution()
print a.maxNumber([3,4,6,5],[9,1,2,5,8,3],5) #[9, 8, 6, 5, 3]
print a.maxNumber([6,7],[6,0,4],5) #[6,7,6,0,4]
print a.maxNumber([3,9],[8,9],3) #[9,8,9]