class Solution:
    def reverse(self, x: int) -> int:
        f = 0
        if x<0:
            x = abs(x)
            f = 1
        s = str(x)[::-1]
        d = ''
        for each in s:
            d = d+ each
        if f == 1:
            d = '-'+d
        if int(d) > math.pow(2,31)-1 or int(d)< math.pow(-2,31):
            d = 0
        return int(d)