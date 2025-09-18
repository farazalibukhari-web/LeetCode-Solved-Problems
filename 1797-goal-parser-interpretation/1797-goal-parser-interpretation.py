class Solution(object):
    def interpret(self, command):
        """
        :type command: str
        :rtype: str
        """
        l=[]
        command=list(command)
        for i in range(len(command)):
            if command[i]=='(':
                if command[i+1]==')':
                    l.append('o')
                else:
                    l.append('al')
            elif command[i]=='G':
                l.append('G')
        return ''.join(l)