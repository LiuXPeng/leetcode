class Solution:
    def solve(self, board):
        """
        :type board: List[List[str]]
        :rtype: void Do not return anything, modify board in-place instead.
        """
        xlength = len(board)
        if xlength == 0:
            return
        ylength = len(board[0])
        def dfs(i, j):
            if board[i][j] == 'Y' or board[i][j] == 'X':
                return
            board[i][j] = 'Y'
            if i > 0:
                dfs(i - 1, j)
            if j > 0:
                dfs(i, j - 1)
            if i + 1 < xlength:
                dfs(i + 1, j)
            if j + 1 < ylength:
                dfs(i, j + 1)
            return
        for i in range(xlength):
            dfs(i, 0)
            dfs(i, ylength - 1)
        for j in range(ylength):
            dfs(0, j)
            dfs(xlength - 1, j)
        for i in range(xlength):
            for j in range(ylength):
                if board[i][j] == 'Y':
                    board[i][j] = 'O'
                else:
                    board[i][j] = 'X'
        return