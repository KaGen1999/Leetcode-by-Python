class Solution:
    def longestPalindrome(self, s: str) -> str:
        n = len(s)
        if n < 2:
            return s
        l = [[False for j in range(n)] for i in range(n)]
        for i in range(n):
            l[i][i] = True
            if i < n - 1:
                l[i][i + 1] = (s[i] == s[i + 1])

        length = 0
        max_s = ''
        for j in range(1, n):
            for i in range(0, j):
                if j != i+1:
                    l[i][j] = True if (l[i + 1][j - 1] and s[i] == s[j]) else False
                if l[i][j] == True and j - i > length:
                    length = j - i
                    max_s = s[i:j + 1]
        if max_s == '':
            return s[0]
        return max_s


if __name__ == '__main__':
    s = Solution()
    r = s.longestPalindrome('ac')
    print(r)
