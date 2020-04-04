class Solution:
    def make2d(self, n, r):
        i = 1
        l = []
        c = int(((n - r) / (r - 1)) + 0.999) + 1
        for t in range(c):
            tmp = [i + j for j in range(r)]
            i = tmp[-1]
            if t % 2 == 1:
                tmp = tmp[::-1]
            l.append(tmp)
        return l, c

    def convert(self, s: str, numRows: int) -> str:
        n = len(s)
        if s == "" or numRows == 1:
            return s
        l, c = self.make2d(n, numRows)
        b = 0
        result = ''
        for i in range(numRows):
            for j in range(c):
                index = l[j][i]
                if index > n:
                    continue
                else:
                    cstr = s[index - 1]
                    if b == index:
                        continue
                    else:
                        result = result + cstr
                        b = index
        return result


if __name__ == '__main__':
    s = Solution()
    # s.make2d(16, 3)
    r = s.convert('PAYPALISHIRING', 4)
    print(r)
