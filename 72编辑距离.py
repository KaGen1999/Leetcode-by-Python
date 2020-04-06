class Solution:
    def minDistance(self, word1: str, word2: str) -> int:
        n = len(word1)
        m = len(word2)
        if n * m == 0:
            return m + n
        l = [[0 for i in range(m + 1)] for _ in range(n + 1)]
        for j in range(m + 1):
            l[0][j] = j
        for i in range(n + 1):
            l[i][0] = i
        for i in range(1, n + 1):
            for j in range(1, m + 1):
                l[i][j] = min(l[i - 1][j] + 1, l[i][j - 1] + 1,
                              l[i - 1][j - 1] if word1[i - 1] == word2[j - 1] else l[i - 1][j - 1] + 1)
        return l[n][m]


if __name__ == '__main__':
    s = Solution()
    r = s.minDistance("horse", "ros")
    print(r)
