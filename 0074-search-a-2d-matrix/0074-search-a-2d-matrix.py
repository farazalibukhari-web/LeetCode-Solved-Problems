class Solution(object):
    def searchMatrix(self, matrix, target):

        # Binary search for find correct row
        up, down = 0, len(matrix) - 1

        # Quick bounds check
        if matrix[0][0] > target or matrix[-1][-1] < target:
            return False

        row = -1  # track if we find a valid row

        while up <= down:
            row_mid = (up + down) // 2
            if matrix[row_mid][0] == target:
                return True
            elif matrix[row_mid][0] < target <= matrix[row_mid][-1]:
                row = row_mid
                break
            elif matrix[row_mid][0] < target:
                up = row_mid + 1
            else:
                down = row_mid - 1

        if row == -1:
            return False  # no valid row found

        # Binary search in the chosen row
        left, right = 0, len(matrix[0]) - 1
        while left <= right:
            col_mid = (left + right) // 2
            if matrix[row][col_mid] == target:
                return True
            elif matrix[row][col_mid] > target:
                right = col_mid - 1
            else:
                left = col_mid + 1

        return False