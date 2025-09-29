class Solution(object):
    def reversePrefix(self, word, ch):
        """
        :type word: str
        :type ch: str
        :rtype: str
        """
        count=0
        new_string=""
        for i in range(len(word)):
            if word[i]==ch and count==0:
                count+=1
                for j in range(i, -1, -1):
                    a=word[j]
                    new_string+=a
            elif count==1:
                new_string+=word[i]
            elif word[i]!=ch and i==len(word)-1:
                return word
        return new_string
