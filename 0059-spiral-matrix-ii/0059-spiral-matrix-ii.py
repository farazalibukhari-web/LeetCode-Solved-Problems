class Solution(object):
    def generateMatrix(self, n):
        """
        :type n: int
        :rtype: List[List[int]]
        """

        matrix = [[0]*n for _ in range(n)]
        row_start,row_end=0,len(matrix)-1
        col_start,col_end=0,len(matrix[0])-1
        num=0
        while row_start<=row_end and col_start<=col_end:
            for col in range(col_start,col_end+1,1):
                num+=1
                matrix[row_start][col]=(num)
            row_start+=1
            for row in range(row_start,row_end+1,1):
                num+=1
                matrix[row][col_end]=(num)
            col_end-=1
            if row_start <= row_end:
                for col in range(col_end,col_start-1,-1):
                    num+=1
                    matrix[row_end][col]=(num)
                row_end-=1
            if col_start<=col_end:
                for row in range(row_end,row_start-1,-1):
                    num+=1
                    matrix[row][col_start]=(num)
                col_start+=1
        return matrix

        