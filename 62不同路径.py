class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        mt = m - 1
        nt = n - 1
        st = mt + nt
        fm = 1
        fz = 1
        s = min(nt, mt)
        for i in range(s):
            fz = fz * st
            st = st - 1
            fm = fm * s
            s = s - 1
        return int(fz / fm)


if __name__ == '__main__':
    s = Solution()
    r = s.uniquePaths(3, 4)
    print(r)
