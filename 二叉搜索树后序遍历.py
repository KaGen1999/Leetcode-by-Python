class Solution:
    def VerifySquenceOfBST(self, sequence):
        # write code here
        def verify(sequence):
            if len(sequence) <= 1:
                return True
            root = sequence[-1]
            l = []
            r = []
            rl = sequence[:-1]
            for i in range(len(rl)):
                if rl[i] > root:
                    l = rl[:i]
                    r = rl[i:]
                    break
            if r == []:
                l = rl
            if r == [] or min(r) > root:
                return verify(l) and verify(r)
            else:
                return False

        return verify(sequence)


if __name__ == '__main__':
    s = Solution()
    print(s.VerifySquenceOfBST([4,6,7,5]))
