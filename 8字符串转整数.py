class Solution:
    def myAtoi(self, str: str) -> int:
        n = ''
        n_s = False
        s_s = False
        for i in str:
            if i == ' ' and not n_s and not s_s:
                continue
            elif ((i == '-' or i == '+') and not n_s and not s_s):
                n = n + i
                s_s = True
            elif i in ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']:
                n = n + i
                # print(n)
                n_s = True
            else:
                break
        if n == '' or n == '-' or n == '+':
            return 0
        num = int(n)
        if num <= -2147483648:
            num = -2147483648
        elif num > 2147483647:
            num = 2147483647
        return num


if __name__ == '__main__':
    s = Solution()
    r = s.myAtoi("   +0 123")
    print(r)
