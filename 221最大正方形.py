class Solution:
    def maximalSquare(self, matrix: List[List[str]]) -> int:
        max_s = 0
        if matrix == []:
            return 0
        n = len(matrix)
        m = len(matrix[0])

        def isSquare(i, j, size):
            for x in range(i, i + size):
                for y in range(j, j + size):
                    if matrix[x][y] == '0':
                        return False
            return True

        for i in range(0, n):
            for j in range(0, m):
                while (not (i + max_s + 1 > n or j + max_s + 1 > m or matrix[i][j] == '0')) and (
                isSquare(i, j, max_s + 1)):
                    max_s = max_s + 1
        return max_s * max_s