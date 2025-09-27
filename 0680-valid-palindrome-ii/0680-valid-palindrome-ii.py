class Solution(object):
    def validPalindrome(self, s):
        """
        :type s: str
        :rtype: bool
        """
        i=0
        j=len(s)-1
        count=0
        while i<=j:
            if s[i]==s[j]:
                i+=1
                j-=1
            elif s[i]!=s[j] and count>=1:
                return False
            elif s[i]!=s[j] and s[j-1]==s[i] and s[j]==s[i+1] :
                i+=1
                j-=1
            elif s[i]!=s[j]:
                if s[i+1]==s[j]:
                    i+=1
                elif s[i]==s[j-1]:
                    j-=1
                count=1
        return True