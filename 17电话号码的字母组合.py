class Solution:
    def letterCombinations(self, digits: str):
        d = {
            '2': ['a', 'b', 'c'],
            '3': ['d', 'e', 'f'],
            '4': ['g', 'h', 'i'],
            '5': ['j', 'k', 'l'],
            '6': ['m', 'n', 'o'],
            '7': ['p', 'q', 'r', 's'],
            '8': ['t', 'u', 'v'],
            '9': ['w', 'x', 'y', 'z']
        }
        result = []
        s = ''
        if digits == '':
            return ''
        def getString(s, digits):
            if digits == '':
                result.append(s)
                return 0
            else:
                for i in d[digits[0]]:
                    getString(s + i, digits[1:])

        getString(s, digits)
        return result


if __name__ == '__main__':
    s = Solution()
    r = s.letterCombinations('23')
    print(r)
