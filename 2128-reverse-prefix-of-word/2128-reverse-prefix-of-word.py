class Solution(object):
    def reversePrefix(self, word, ch):
        """
        :type word: str
        :type ch: str
        :rtype: str
        """
        if ch not in word:
            return word
        i=word.index(ch)
        new_string=word[:i+1][::-1]+word[i+1:]
        
        return new_string