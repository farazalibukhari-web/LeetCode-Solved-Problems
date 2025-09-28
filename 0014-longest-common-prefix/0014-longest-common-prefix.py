class Solution(object):
    def longestCommonPrefix(self, strs):
        """
        :type strs: List[str]
        :rtype: str
        """
        word_1=list("".join(strs[0]))
        for i in range(1,len(strs)):
            new_list=[]
            word_2=list("".join(strs[i]))
            for j in range(min(len(word_1),len(word_2))):
                if word_1[j]==word_2[j]:
                    new_list.append(word_1[j])              
                else:
                    break
            word_1=new_list[::]
            
        return "".join(word_1)
                