class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        t = ''
        if strs == [] or '' in strs:
            return t
        if len(strs) == 1:
            return strs[0]
        a = strs[-1]
        strs.pop()
        for i in range(len(a)):
            for each in strs:
                if i + 1 > len(each):
                    return t
                if a[i] != each[i]:
                    return t
            t = t + a[i]
        return t
