class Solution:
    def exist(self, board, word: str):
        n = len(board)
        m = len(board[0])

        def get_ans(board, i, j, t):
            if t == len(word):
                return True
            if i < 0 or i >= n or j < 0 or j >= m:
                return False

            if board[i][j] == word[t]:
                board[i][j] = None
                r = get_ans(board, i, j - 1, t + 1) or get_ans(board, i, j + 1, t + 1) or get_ans(board, i - 1, j,t + 1) or get_ans(board, i + 1, j, t + 1)
                board[i][j] = word[t]
                return r

        for i in range(n):
            for j in range(m):
                if get_ans(board, i, j, 0):
                    return True
        return False


if __name__ == '__main__':
    s = Solution()
    r = s.exist([["C", "A", "A"],
                 ["A", "A", "A"],
                 ["B", "C", "D"]], "AAB")
    print(r)