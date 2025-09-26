class Solution(object):
    def isPalindrome(self, s):
        """
        :type s: str
        :rtype: bool
        """
        s = s.lower()
        i, j = 0, len(s) - 1
        
        while i < j:
            # skip non-alphanumeric on left
            if not s[i].isalnum():
                i += 1
                continue
            # skip non-alphanumeric on right
            if not s[j].isalnum():
                j -= 1
                continue
            
            # compare
            if s[i] != s[j]:
                return False
            
            i += 1
            j -= 1
        
        return True
