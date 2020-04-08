class Solution:
    def uniquePathsWithObstacles(self, obstacleGrid) -> int:
        if obstacleGrid[-1][-1] == 1:
            return 0
        m = len(obstacleGrid)
        n = len(obstacleGrid[0])
        l = [[0 for _ in range(n)] for _ in range(m)]
        l[0] = [1 for _ in range(n)]
        for i in range(m):
            for j in range(n):
                if i == 0 and j == 0:
                    continue
                if i == 0:
                    l[i][j] = (l[i][j - 1] if obstacleGrid[i][j - 1] == 0 else 0)
                elif j == 0:
                    l[i][j] = (l[i - 1][j] if obstacleGrid[i - 1][j] == 0 else 0)
                else:
                    l[i][j] = (l[i][j - 1] if obstacleGrid[i][j - 1] == 0 else 0) + (
                        l[i - 1][j] if obstacleGrid[i - 1][j] == 0 else 0)

        return l[m - 1][n - 1]


if __name__ == '__main__':
    s = Solution()
    r = s.uniquePathsWithObstacles(
        [[0, 1], [0, 0]]
    )
    print(r)
