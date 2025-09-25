class Solution(object):
    def reverseWords(self, s):
        """
        :type s: str
        :rtype: str
        """
        new_s = s.split(" ")
        for word in range(len(new_s)):
            new_s[word] = new_s[word][::-1]
        return " ".join(new_s)