class Solution(object):
    def longestConsecutive(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        st=set(nums)
        res=0
        while st:
            k=st.pop()
            a,b=k+1,k-1
            while a in st:
                st.remove(a)
                a+=1
            while b in st:
                st.remove(b)
                b-=1
            res=max(res,(a-k-1)+(k-1-b)+1)
        return res
        
a=Solution()
print a.longestConsecutive([100, 4, 200, 1, 3, 2]) #4