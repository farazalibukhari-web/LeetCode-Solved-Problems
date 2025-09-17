class Solution(object):
    def restoreString(self, s, indices):
        """
        :type s: str
        :type indices: List[int]
        :rtype: str
        """
        ans = [""] * len(s) 
        for i, ch in enumerate(s):
            ans[indices[i]] = ch

        return "".join(ans)