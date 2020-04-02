class Solution:
    def maxDepthAfterSplit(self, seq: str) -> List[int]:
        n = len(seq)
        l = [0 for i in range(n)]
        a = 0
        b = 0
        for index, each in enumerate(seq):
            # print(index, each, a, b)
            if each == '(':
                if a <= b:
                    a = a + 1
                    l[index] = 0
                else:
                    b = b + 1
                    l[index] = 1
            else:
                if b != 0:
                    l[index] = 1
                    b = b - 1
                else:
                    l[index] = 0
                    a = a - 1
        return l
