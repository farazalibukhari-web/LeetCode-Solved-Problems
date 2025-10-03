class Solution(object):
    def setZeroes(self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: None Do not return anything, modify matrix in-place instead.
        """
        len_row,len_col=len(matrix),len(matrix[0])
        zero_row=set()
        zero_col=set()
        
        #noting the positions of zeros
        for row in range(len_row):
            for col in range(len_col):
                if matrix[row][col]==0:
                    zero_row.add(row)
                    zero_col.add(col)
                
        #updating the rows
        for i in zero_row:
            for j in range(len_col):
                matrix[i][j]=0
        
        #updating the rows
        for j in zero_col:
            for i in range(len_row):
                matrix[i][j]=0
        
        return matrix

        
        