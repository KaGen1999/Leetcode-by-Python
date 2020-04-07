class Solution:
    def rotate(self, matrix):
        """
        Do not return anything, modify matrix in-place instead.
        """
        n = len(matrix[0])
        for i in range(n):
            for j in range(n):
                matrix[j][n - 1 - i] = str(matrix[j][n - 1 - i]) + '|' + str(int(str(matrix[i][j]).split('|')[0]))
        for i in range(n):
            for j in range(n):
                matrix[i][j] = int(matrix[i][j].split('|')[1])
        for each in matrix:
            print(each)


if __name__ == '__main__':
    s = Solution()
    s.rotate([[43, 39, 3, 33, 37, 20, 14],
              [9, 18, 9, -1, 40, 22, 38],
              [14, 42, 3, 23, 12, 14, 32],
              [18, 31, 45, 11, 8, -1, 31],
              [28, 44, 14, 23, 40, 24, 13],
              [29, 45, 33, 45, 20, 0, 45],
              [12, 23, 35, 32, 22, 39, 8]])
