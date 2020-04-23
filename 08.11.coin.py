class Solution:
    def waysToChange(self, n: int) -> int:
        if n == 0:
            return 0
        l = [[1 for _ in range(n+1)] for i in range(4)]
        c = [1,5,10,25]
        for i in range(1,4):
            for j in range(1,n+1):
                if j < c[i]:
                    l[i][j] = l[i-1][j]
                else:
                    l[i][j] = l[i-1][j] + l[i][j-c[i]]
        return l[-1][-1] % 1000000007