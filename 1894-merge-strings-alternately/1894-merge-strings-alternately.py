class Solution(object):
    def mergeAlternately(self, word1, word2):
        """
        :type word1: str
        :type word2: str
        :rtype: str
        """
        merge_string = []
        i,j= 0,0
        while i < len(word1) and j < len(word2):
            merge_string.append(word1[i])
            merge_string.append(word2[j])
            i +=1
            j += 1
        if i < len(word1):
            merge_string.append(word1[i:])
        if j < len(word2):
            merge_string.append(word2[j:])

        return "".join(merge_string)