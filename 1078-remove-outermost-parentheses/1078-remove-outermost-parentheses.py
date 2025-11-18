class Solution(object):
    def removeOuterParentheses(self, s):
        """
        :type s: str
        :rtype: str
        """
        res = ""
        count = 0   # keeps track of open parentheses

        for ch in s:
            if ch == '(':
                if count > 0:     # not the outermost '('
                    res += '('
                count += 1
            else:
                count -= 1
                if count > 0:     # not the outermost ')'
                    res += ')'
        return res