class Solution:
    def longestCommonPrefix(self, strs):
        """
        :type strs: List[str]
        :rtype: str
        """
        if not strs: return ""
        res=strs[0]
        for string in strs:
            for i in range(len(res)):
                if i==len(string) or res[i]!=string[i]:
                    res=res[:i]
                    break
        return res