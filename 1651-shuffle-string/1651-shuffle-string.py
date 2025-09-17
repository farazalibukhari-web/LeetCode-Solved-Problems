class Solution(object):
    def restoreString(self, s, indices):
        """
        :type s: str
        :type indices: List[int]
        :rtype: str
        """
        new_str=""
        new_indices=indices[:]
        new_indices.sort()
        for i in new_indices:
            j=indices.index(i)
            new_str+=s[j]
        return new_str