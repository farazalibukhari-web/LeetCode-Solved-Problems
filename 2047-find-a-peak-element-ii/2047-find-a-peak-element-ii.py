class Solution(object):
    def findPeakGrid(self,mat):
        row, col = len(mat), len(mat[0])
        left, right = 0, col - 1

        while left <= right:
            mid_col = (left + right) // 2

            # Find the row index of the maximum element in mid_col
            max_row = 0
            for row_num in range(row):
                if mat[row_num][mid_col] > mat[max_row][mid_col]:
                    max_row = row_num
            
            curr_val  = mat[max_row][mid_col]
            if mid_col - 1 >= 0:
                left_val  = mat[max_row][mid_col - 1] 
            else:
                left_val  = -1
            if mid_col + 1 < col:
                right_val = mat[max_row][mid_col + 1] 
            else:
                right_val = -1
            
            # Compare with left and right neighbors
            if curr_val > left_val and curr_val > right_val:
                return [max_row, mid_col]
            elif right_val > curr_val:
                left = mid_col + 1
            else:
                right = mid_col - 1

        return [-1, -1]