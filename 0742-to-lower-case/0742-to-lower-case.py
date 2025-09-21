class Solution(object):
    def toLowerCase(self, s):
        """
        :type s: str
        :rtype: str
        """
        new_string = ""
        for letter in s:
            if 'A' <= letter <= 'Z':  
                new_string += chr(ord(letter) + 32)
            else:
                new_string += letter       
        return new_string