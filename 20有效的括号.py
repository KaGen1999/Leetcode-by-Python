class Solution:
    def isValid(self, s: str) -> bool:
        if s == '':
            return True
        n = len(s)
        if n % 2 == 1:
            return False
        l = []
        for each in s:
            if each == '(':
                l.append(')')
            elif each == '{':
                l.append('}')
            elif each == '[':
                l.append(']')
            elif each == ')' or each == '}' or each == ']':
                if len(l) != 0 and each != l.pop():
                    return False
        if len(l) != 0:
            return False
        return True


if __name__ == '__main__':
    s = Solution()
    r = s.isValid('){')
    print(r)
