class Solution:
    def numIslands(self, grid) -> int:
        def down_land(i, j, m, n):
            if i < 0 or j < 0 or i >= n or j >= m:
                return 0
            if grid[i][j] == '1':
                grid[i][j] = '0'
                down_land(i - 1, j, m, n)
                down_land(i + 1, j, m, n)
                down_land(i, j - 1, m, n)
                down_land(i, j + 1, m, n)

        if grid == []:
            return 0
        n = len(grid)
        m = len(grid[0])

        land = 0
        for i in range(n):
            for j in range(m):
                if grid[i][j] == '1':
                    land = land + 1
                    down_land(i, j, m, n)
        return land


if __name__ == '__main__':
    s = Solution()
    s.numIslands([["1","1","1","1","0"],["1","1","0","1","0"],["1","1","0","0","0"],["0","0","0","0","0"]])
