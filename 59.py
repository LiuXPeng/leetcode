class Solution:
    def generateMatrix(self, n):
        """
        :type n: int
        :rtype: List[List[int]]
        """
        number = 1
        res = [[None for col in range(n)] for row in range(n)]
        #每次写数，都把一行/列写满
        for k in range(n):
            #上
            for i in range(k, n - k):
                res[k][i] = number
                number += 1
            #右
            for i in range(k + 1, n - k):
                res[i][n - k - 1] = number
                number += 1
            #下
            for i in range(n - k - 2, k - 1, -1):
                res[n - 1 - k][i] = number
                number += 1
            #左
            for i in range(n - k - 2, k, -1):
                res[i][k] = number
                number += 1
        return res