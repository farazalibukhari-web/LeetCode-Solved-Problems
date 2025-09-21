class Solution(object):
    def arrayStringsAreEqual(self, word1, word2):
        """
        :type word1: List[str]
        :type word2: List[str]
        :rtype: bool
        """
        word1_list=list("".join(word1))
        word2_list=list("".join(word2))
        i=0
        if len(word1_list)==len(word2_list):
            while i<len(word1_list):
                if word1_list[i]==word2_list[i]:
                    i+=1
                else:
                    return False
            return True
        else:
            return False