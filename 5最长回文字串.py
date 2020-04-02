class Solution:
    def judge_str(self, s):
        if s == s[::-1]:
            return True
        else:
            return False

    def longestPalindrome(self, s: str) -> str:
        n = len(s)
        if n == 1:
            return s
        elif n == 0:
            return ''
        r = s[0]
        for i in range(n):
            for j in range(i + 1, n):
                tmp_s = s[i:j+1]
                # print(tmp_s)
                if self.judge_str(tmp_s) and len(tmp_s) > len(r):
                    r = tmp_s
        return r


if __name__ == '__main__':
    s = Solution()
    r = s.longestPalindrome('abab')
    print(r)
