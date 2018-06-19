class Solution:
    def rotate(self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: void Do not return anything, modify matrix in-place instead.
        """
        length = len(matrix)
        for i in range((length + 1)// 2):
            for j in range(length // 2):
                temp = matrix[i][j]
                matrix[i][j] = matrix[length - j - 1][i]
                matrix[length - j - 1][i] = matrix[length - 1 - i][length - 1 - j]
                matrix[length - 1 - i][length - 1 - j] = matrix[j][length - 1 - i]
                matrix[j][length - 1 - i] = temp
        return               