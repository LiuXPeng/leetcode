class Solution:
    def spiralOrder(self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: List[int]
        """
        m = len(matrix)
        if m == 0:
            return []
        n = len(matrix[0])
        if n == 0:
            return []
        res = []
        if m > n:
            k = n
        else:
            k = m
        for i in range(k // 2):
            for j in range(i, n - i):
                res.append(matrix[i][j])
            for j in range(i + 1, m - i):
                res.append(matrix[j][n - i - 1])
            for j in range(n - i - 2, i - 1, - 1):
                res.append(matrix[m - i - 1][j])
            for j in range(m - i - 2, i, - 1):
                res.append(matrix[j][i])
        if k % 2 == 1:
            i = k // 2
            if n > m:
                for j in range(i, n - i):
                    res.append(matrix[i][j])
            else:
                for j in range(i, m - i):
                    res.append(matrix[j][i])
        return res