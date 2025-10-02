class Solution(object):
    def spiralMatrixIII(self, rows, cols, rStart, cStart):
        """
        :type rows: int
        :type cols: int
        :type rStart: int
        :type cStart: int
        :rtype: List[List[int]]
        """
        direction=[[0,1],[1,0],[0,-1],[-1,0]]
        new_list=[]
        step=1
        i=0
        row_start,col_start=rStart, cStart
        new_list.append([row_start,col_start])

        while len(new_list)< rows*cols:
            for a in range(2):
                row_direction,col_direction=direction[i % 4]
                for b in range(step):
                    row_start+=row_direction
                    col_start+=col_direction
                    if 0<= row_start< rows and 0<= col_start< cols:
                        new_list.append([row_start,col_start])
                i+=1
            step+=1
        return new_list