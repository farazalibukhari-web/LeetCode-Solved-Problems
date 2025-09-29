class Solution(object):
    def mergeAlternately(self, word1, word2):
        """
        :type word1: str
        :type word2: str
        :rtype: str
        """
        new_string=""
        large_string=max(word1, word2, key=len)
        small_string=min(word1, word2, key=len)
        for i in range(len(large_string)):
            if i<len(small_string):
                new_string+=word1[i]+word2[i]
            else:
                new_string+=large_string[i]
        return new_string