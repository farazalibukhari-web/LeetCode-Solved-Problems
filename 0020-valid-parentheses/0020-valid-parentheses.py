class Solution(object):
    def isValid(self, s):
        """
        :type s: str
        :rtype: bool
        """
        stack = []
        para_dic = {')': '(', '}': '{', ']': '['}
        for para in s:
            if para in para_dic:
                if not stack or stack[-1] != para_dic[para]:
                    return False
                stack.pop()
            else:
                stack.append(para)
        return len(stack) == 0