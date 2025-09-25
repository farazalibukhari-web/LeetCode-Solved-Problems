class Solution(object):
    def reverseWords(self, s):
        """
        :type s: str
        :rtype: str
        """
        new_s=""
        new_list=s.split()
        for word in new_list:
            new_list2=list("".join(word))
            new_list2=new_list2[::-1]
            new_s+=("".join(new_list2))+" "
        return new_s.strip()