class Solution(object):
    def judgeCircle(self, moves):
        """
        :type moves: str
        :rtype: bool
        """
        count_1=0
        count_2=0
        for i in range(len(moves)):
            if moves[i]=="U":
                count_1+=1
            elif moves[i]=="D":
                count_1-=1
            elif moves[i]=="L":
                count_2-=1
            else:
                count_2+=1
        if count_1==0 and count_2==0:
            return True
        else:
            return False
            
            