import copy


class Solution:
    def solveNQueens(self, n: int):
        def toQ(sec, row, l, leftx, rightx):
            for i in range(n):
                if i not in l and i + row not in leftx and row - i not in rightx:
                    sec[row][i] = "Q"
                    l.add(i)
                    leftx.add(i + row)
                    rightx.add(row - i)
                    if row == n - 1:
                        result.append(copy.deepcopy(sec))
                        l.remove(i)
                        leftx.remove(i + row)
                        rightx.remove(row - i)
                        sec[row][i] = '.'
                        return
                    else:
                        toQ(sec, row + 1, l, leftx, rightx)
                        l.remove(i)
                        leftx.remove(i + row)
                        rightx.remove(row - i)
                        sec[row][i] = '.'
                        # return

        result = []
        l = set()
        leftx = set()
        rightx = set()
        sec = [['.' for i in range(n)] for i in range(n)]
        toQ(sec, 0, l, leftx, rightx)
        r = []
        for l in result:
            msg = []
            for each in l:
                msg.append(''.join(each))
            r.append(msg)
        # print(r)
        return r


if __name__ == '__main__':
    s = Solution()
    s.solveNQueens(4)
