class Solution(object):
    def spiralOrder(self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: List[int]
        """
        row_start, row_end = 0, len(matrix) - 1
        col_start, col_end = 0, len(matrix[0]) - 1
        new_list = []

        while row_start <= row_end and col_start <= col_end:
            # 1. Traverse left → right
            for col in range(col_start, col_end + 1):
                new_list.append(matrix[row_start][col])
            row_start += 1

            # 2. Traverse top → bottom
            for row in range(row_start, row_end + 1):
                new_list.append(matrix[row][col_end])
            col_end -= 1

            # 3. Traverse right → left (check row validity)
            if row_start <= row_end:
                for col in range(col_end, col_start - 1, -1):
                    new_list.append(matrix[row_end][col])
                row_end -= 1

            # 4. Traverse bottom → top (check column validity)
            if col_start <= col_end:
                for row in range(row_end, row_start - 1, -1):
                    new_list.append(matrix[row][col_start])
                col_start += 1

        return new_list