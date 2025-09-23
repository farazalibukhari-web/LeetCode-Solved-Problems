class Solution(object):
    def freqAlphabets(self, s):
        """
        :type s: str
        :rtype: str
        """
        new_string=""
        pos=0
        while pos<=len(s)-1:
            if pos+2<len(s)  and s[pos+2]== '#':
                num = int(s[pos:pos+2]) 
                new_string += chr(96 + num)
                pos += 3 
            else:
                num = int(s[pos])           # single digit
                new_string += chr(96 + num)
                pos += 1
        return new_string
