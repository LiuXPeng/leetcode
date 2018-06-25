class Solution:
    def setZeroes(self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: void Do not return anything, modify matrix in-place instead.
        """
        label = False
        m = len(matrix)
        n = len(matrix[0])
        for i in range(n):
            if matrix[0][i] == 0:
                label = True
                break
        for i in range(1, m):
            label2 = False
            for j in range(n):
                if matrix[i][j] == 0:
                    matrix[0][j] = 0
                    label2 = True
            if label2:
                for j in range(n):
                    matrix[i][j] = 0
        for j in range(n):
            if matrix[0][j] == 0:
                for i in range(m):
                    matrix[i][j] = 0
        if label:
            for j in range(n):
                matrix[0][j] = 0
        return