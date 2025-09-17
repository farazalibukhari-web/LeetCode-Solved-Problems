class Solution(object):
    def defangIPaddr(self, address):
        """
        :type address: str
        :rtype: str
        """
        new_address=""
        for i in address:
            if i == ".":         
                new_address += "[.]"      
            else:
                new_address += i   
                
        return new_address