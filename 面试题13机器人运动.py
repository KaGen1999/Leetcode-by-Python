class Solution:
    def movingCount(self, m: int, n: int, k: int) -> int:
        l = [[False for _ in range(n)] for _ in range(m)]
        l[0][0] = True
        result = 1
        for i in range(m):
            for j in range(n):
                sm = i
                sn = j
                if sm >= 10:
                    sm = int(i / 10) + i % 10
                if sn >= 10:
                    sn = int(j / 10) + j % 10
                s = sm + sn
                # print(s)
                if s <= k and ((False if j == 0 else l[i][j - 1]) or (False if i == 0 else l[i - 1][j])):
                    l[i][j] = True
                    result = result + 1
        # for each in l:
        #     print(each)
        return result


if __name__ == '__main__':
    s = Solution()
    r = s.movingCount(8, 11, 16)
    print(r)
