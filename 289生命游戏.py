class Solution:
    def get_sum(self, board, i, j):
        s = board[i - 1][j] + board[i][j - 1] + board[i + 1][j] + board[i][j + 1] + board[i - 1][j - 1] + board[i - 1][
            j + 1] + board[i + 1][j - 1] + board[i + 1][j + 1]
        return s

    def gameOfLife(self, board):
        """
        Do not return anything, modify board in-place instead.
        """
        c, r = len(board[0]), len(board)
        # 扩充一圈0
        new_board = [[0 for i in range(c + 2)]]
        for index, each in enumerate(board):
            new_board = new_board + [[0] + each + [0]]
        new_board = new_board + [[0 for i in range(c + 2)]]

        # for each in new_board:
        #     print(each)
        for i in range(1, r + 1):
            for j in range(1, c + 1):
                s = self.get_sum(new_board, i, j)
                if new_board[i][j] == 1 and (s < 2 or s > 3):
                    board[i - 1][j - 1] = 0
                elif new_board[i][j] == 1 and (s == 3 or s == 2):
                    board[i - 1][j - 1] = 1
                elif new_board[i][j] == 0 and s == 3:
                    board[i - 1][j - 1] = 1

        # return board


if __name__ == '__main__':
    s = Solution()
    # s.gameOfLife([
    #     [0, 1, 0],
    #     [0, 0, 1],
    #     [1, 1, 1],
    #     [0, 0, 0]
    # ])
