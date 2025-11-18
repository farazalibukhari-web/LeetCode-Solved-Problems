class Solution(object):
    def removeOuterParentheses(self, s):
        """
        :type s: str
        :rtype: str
        """
        result = []
        stack = []

        for ch in s:
            if ch == '(':        
                if len(stack)>0:
                    result.append(ch)
                stack.append('(')
            else:  # ch == ')'
                stack.pop()               
                if len(stack)>0:
                    result.append(ch)

        return "".join(result)

                
