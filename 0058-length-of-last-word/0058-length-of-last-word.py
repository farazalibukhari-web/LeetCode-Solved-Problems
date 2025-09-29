class Solution(object):
    def lengthOfLastWord(self, s):
        """
        :type s: str
        :rtype: int
        """
        new_list=list(s.split())
        length=len("".join(new_list[-1:]))
        return length