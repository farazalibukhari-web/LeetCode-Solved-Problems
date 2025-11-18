class Solution(object):
    def removeDuplicates(self, s):
        """
        :type s: str
        :rtype: str
        """
        string = ""

        for c in s:
            if len(string) == 0 or string[-1] != c:
                string += c
            else:
                string = string[:-1]
        
        return string