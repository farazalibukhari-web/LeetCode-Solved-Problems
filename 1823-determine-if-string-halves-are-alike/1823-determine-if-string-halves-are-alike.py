class Solution(object):
    def halvesAreAlike(self, s):
        """
        :type s: str
        :rtype: bool
        """
        count_1=0
        count_2=0
        n=len(s)//2
        list_1=list("".join(s[:n]))
        list_2=list("".join(s[n:]))
        for letter in list_1:
            if letter in "aeiouAEIOU":
                count_1+=1
                
        for letter in list_2:
            if letter in "aeiouAEIOU":
                count_2+=1
        if count_1==count_2:
            return True
        return False        