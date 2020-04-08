# class Solution:
#     def climbStairs(self, n: int) -> int:
#         if n == 1 or n == 2:
#             return n
#         l = [1 for i in range(n)]
#         l[1] = 2
#         for i in range(2, n):
#             l[i] = l[i - 1] + l[i - 2]
#         print(l)
#         return l[n - 1]

class Solution:
    def climbStairs(self, n: int) -> int:
        if n == 1 or n == 2:
            return n
        a = 1
        b = 2
        for i in range(2,n):
            l = a+b
            a = b
            b = l
        return l

if __name__ == '__main__':
    s = Solution()
    s.climbStairs(3)
