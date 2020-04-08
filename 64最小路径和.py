class Solution:
    def minPathSum(self, grid) -> int:
        m = len(grid)
        n = len(grid[0])
        d = [[0 for i in range(n)] for _ in range(m)]
        for i in range(m):
            for j in range(n):
                if i == 0:
                    d[i][j] = d[i][j - 1] + grid[i][j]
                elif j == 0:
                    d[i][j] = d[i - 1][j] + grid[i][j]
                else:
                    d[i][j] = min(d[i - 1][j], d[i][j - 1]) + grid[i][j]
        for each in d:
            print(each)
        return d[m - 1][n - 1]


if __name__ == '__main__':
    s = Solution()
    r = s.minPathSum([
  [1,3,1],
  [1,5,1],
  [4,2,1]
])
    print(r)
