class Solution:
    def exist(self, board, word):
        """
        :type board: List[List[str]]
        :type word: str
        :rtype: bool
        """
        n = len(board)
        m = len(board[0])
        def method(board, loc, x, y):
            if word[loc] == board[x][y]:
                if loc == len(word) - 1:
                    return True
                temp = board[x][y]
                board[x][y] = False
                if x >= 1:
                    if method(board, loc + 1, x - 1, y):
                        return True
                if x < n - 1:
                    if method(board, loc + 1, x + 1, y):
                        return True
                if y >= 1:
                    if method(board, loc + 1, x, y - 1):
                        return True
                if y < m - 1:
                    if method(board, loc + 1, x, y + 1):
                        return True
                board[x][y] = temp
            return False
        for i in range(n):
            for j in range(m):
                if method(board, 0, i, j):
                    return True
        return False