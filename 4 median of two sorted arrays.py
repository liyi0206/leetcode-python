class Solution(object):
    def findMedianSortedArrays(self, nums1, nums2):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: float
        """
        totlen=len(nums1)+len(nums2)
        if totlen&1:
            return self.findK(nums1,nums2,(totlen+1)/2)
        else:
            return (self.findK(nums1,nums2,totlen/2)+self.findK(nums1,nums2,totlen/2+1))/2.0
        
    def findK(self,A,B,K):
        la,lb=len(A),len(B)
        pa=min(la,K/2)
        pb=K-pa
        if la>lb: return self.findK(B,A,K)
        if la==0: return B[K-1]
        if K==1: return min(A[0],B[0]) #worst case
        if A[pa-1]<B[pb-1]: return self.findK(A[pa:],B,K-pa)
        elif A[pa-1]>B[pb-1]: return self.findK(A,B[pb:],K-pb)
        else: return A[pa-1]
            
# notes!
# 1, /2.0
# 2, k-1,pa-1,pb-1

# time complexity - o(log(min(m,n)))