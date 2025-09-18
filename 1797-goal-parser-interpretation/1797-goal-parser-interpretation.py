class Solution(object):
    def interpret(self, command):
        """
        :type command: str
        :rtype: str
        """
        i=0
        new_str=""
        while i<len(command):
            if command[i]=="G":
                new_str+="G"
                i+=1
            elif command[i:i+2]=="()":
                new_str+="o"
                i+=2
            elif command[i:i+4]=="(al)":
                new_str+="al"
                i+=4
        return new_str