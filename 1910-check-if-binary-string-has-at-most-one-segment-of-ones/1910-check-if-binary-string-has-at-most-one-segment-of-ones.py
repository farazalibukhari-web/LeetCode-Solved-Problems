class Solution(object):
    def checkOnesSegment(self, s):
        """
        :type s: str
        :rtype: bool
        """
        count_repeat=0
        for i in range(len(s)):
            if s[i]=="1" and (i==0 or s[i-1]=="0"):
                count_repeat+=1
        return count_repeat==1

                
