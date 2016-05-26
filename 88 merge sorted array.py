class Solution(object):
    def merge(self, nums1, m, nums2, n):
        """
        :type nums1: List[int]
        :type m: int
        :type nums2: List[int]
        :type n: int
        :rtype: void Do not return anything, modify nums1 in-place instead.
        """
        p1,p2,p = m-1,n-1,m+n-1
        while p1>=0 and p2>=0:
            if nums1[p1]>=nums2[p2]:
                nums1[p]=nums1[p1]
                p,p1=p-1,p1-1
            else:
                nums1[p]=nums2[p2]
                p,p2=p-1,p2-1
        if p2>=0:
            nums1[0:p2+1]=nums2[0:p2+1]

a=Solution()
nums1,nums2=[1,3,5,0,0],[2,4]
a.merge(nums1,3,nums2,2)
print nums1

nums1,nums2=[2,4,0,0,0],[1,3,5]
a.merge(nums1,2,nums2,3)
print nums1

nums1,nums2=[0],[1]
a.merge(nums1,0,nums2,1)
print nums1