# 动态规划，类似楼梯问题
class Solution:
    def numDecodings(self, s: str) -> int:
        n = len(s)
        if n == 0 or s[0] == '0':
            return 0
        if n == 1:
            return 1
        w = [0 for i in range(n+1)]
        w[0] = 1
        w[1] = 1
        for i in range(1,n):
            if s[i-1] !='1' and s[i-1]!='2':
                if s[i] == '0':
                    return 0
                else:
                    w[i+1] = w[i]
            else:
                if s[i] == '0':
                    w[i+1] = w[i-1]
                else:
                    if int(s[i-1] + s[i]) > 26:
                        w[i+1] = w[i]
                    else:
                        w[i+1] = w[i] + w[i-1]
        return w[-1]