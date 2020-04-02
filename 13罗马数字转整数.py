class Solution:
    def romanToInt(self, s: str) -> int:
        d={
            'I':1,
            'V':5,
            'X':10,
            'L':50,
            'C':100,
            'D':500,
            'M':1000,
        }
        sum_ = 0
        for i in range(len(s)):
            if i+1 == len(s) or d[s[i]] >= d[s[i+1]]:
                sum_ = sum_ + d[s[i]]
            else:
                sum_ = sum_ - d[s[i]]
        return sum_