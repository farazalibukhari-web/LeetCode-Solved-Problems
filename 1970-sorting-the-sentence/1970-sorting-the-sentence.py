class Solution(object):
    def sortSentence(self, s):
        """
        :type s: str
        :rtype: str
        """
        words = s.split()

        new_list=[""]*len(words)
        for token in words:
            word = token[:-1]
            index = int(token[-1])-1
            new_list[index]=word
        new_s=" ".join(new_list)
        return new_s