class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        l = sorted(intervals)
        print(l)
        n = len(l)
        r = []
        jmp = 0
        for i in range(n):
            if jmp == 1:
                jmp = 0
                continue
            if i == n - 1:
                r.append(l[i])
            if l[i][1] >= l[i + 1][0]:
                r.append([l[i][0], l[i + 1][1]])
                jmp = 1
            else:
                jmp = 0
                r.append(l[i])
        return r
