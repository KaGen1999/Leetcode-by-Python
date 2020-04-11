class Solution:
    def reverseWords(self, s: str) -> str:
        l = s.split(' ')
        l = l[::-1]
        s = ''
        for each in l:
            if each != '':
                s = s + each + ' '
        return s.strip()