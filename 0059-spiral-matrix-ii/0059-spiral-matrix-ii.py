class Solution(object):
    def generateMatrix(self, n):
        """
        :type n: int
        :rtype: List[List[int]]
        """

        res, i, val =[[0]*n for _ in range(n)], 0, 1
        while val <= n*n:
            for r in range(i, n - i): res[i][r] = val; val += 1
            for r in range(i + 1, n - i): res[r][n - i - 1] = val; val += 1
            for r in range(n - i - 2, i - 1, -1): res[n - i - 1][r] = val; val += 1
            for r in range(n - i - 2, i, -1): res[r][i] = val; val += 1
            i += 1
        return res

        