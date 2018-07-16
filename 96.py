class Solution:
    def numTrees(self, n):
        """
        :type n: int
        :rtype: int
        """
        if n == 0 or n == 1:
            return 1
        DP = [1, 1]
        for i in range(2, n + 1):
            temp = 0
            for j in range(i):
                temp = temp + DP[j] * DP[i - j - 1]
            DP.append(temp)
        return DP[-1]