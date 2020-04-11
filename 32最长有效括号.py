class Solution:
    def longestValidParentheses(self, s: str) -> int:
        n = len(s)
        d = [0 for _ in range(n)]
        max_num = 0
        for i in range(1,n):
            if s[i] == ')' and s[i-1] == '(':
                d[i] = d[i-2] + 2
            elif s[i] == ')' and s[i-1] == ')':
                if i - d[i-1] -1 >=0:
                    if s[i - d[i-1] -1] == '(':
                        d[i] = d[i-1] + d[i-d[i-1]-2] + 2
                else:
                    d[i] = 0
            if d[i] > max_num:
                max_num = d[i]
        return max_num        