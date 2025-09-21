class Solution(object):
    def halvesAreAlike(self, s):
        """
        :type s: str
        :rtype: bool
        """
        count_1=0
        count_2=0
        new_list=list("".join(s))
        for letter in range(len(new_list)):
            if new_list[letter] in "aeiouAEIOU":
                if letter<=(len(new_list)-1)//2:
                    count_1+=1
                else:
                    count_2+=1
        if count_1==count_2:
            return True
        else:
            return False       