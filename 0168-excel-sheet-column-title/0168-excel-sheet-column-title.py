class Solution(object):
    def convertToTitle(self, columnNumber):
        """
        :type columnNumber: int
        :rtype: str
        """
        new_string=""
        while columnNumber>0:
            columnNumber-=1
            reminder=columnNumber%26
            columnNumber=columnNumber//26
            new_string+=chr(reminder+65)
        new_string=new_string[::-1]
        return new_string