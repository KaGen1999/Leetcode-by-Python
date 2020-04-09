class Solution:
    def generateParenthesis(self, n: int):
        result = []
        s = ''

        def getstring(left, right, s):
            if left == n and right == n:
                result.append(s)
                return 0
            else:
                if left > right and left <= n:
                    s = s + ')'
                    getstring(left, right + 1, s)
                    # 回退 再进行情况2
                    s = s[:-1] + '('
                    getstring(left + 1, right, s)
                if left == right:
                    s = s + '('
                    getstring(left + 1, right, s)

        getstring(0, 0, s)
        print(result)
        return result


if __name__ == '__main__':
    s = Solution()
    r = s.generateParenthesis(1)
    print(r)
