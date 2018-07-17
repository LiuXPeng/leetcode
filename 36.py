class Solution:
    def isValidSudoku(self, board):
        """
        :type board: List[List[str]]
        :rtype: bool
        """
        for i in range(9):
            for j in range(9):
                if board[i][j] == '.':
                    continue
                for k in range(9):
                    if board[i][k] == board[i][j] and k != j:
                        return False
                for k in range(9):
                    if board[k][j] == board[i][j] and k != i:
                        return False
                for m in range((i // 3) * 3, (i // 3) * 3 + 3):
                    for n in range((j // 3) * 3, (j // 3) * 3 + 3):
                        if board[m][n] == board[i][j]:
                            if m != i or n != j:
                                return False
        return True