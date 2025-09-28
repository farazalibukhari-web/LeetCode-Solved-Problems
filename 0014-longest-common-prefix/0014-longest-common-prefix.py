class Solution(object):
    def longestCommonPrefix(self, strs):
        """
        :type strs: List[str]
        :rtype: str
        """
        prefix = strs[0]
        for word in strs[1:]:
            j = 0
            while j < len(prefix) and j < len(word) and prefix[j] == word[j]:
                j += 1
            prefix = prefix[:j]
            if not prefix:   # no common prefix, break early
                break
        return prefix
                