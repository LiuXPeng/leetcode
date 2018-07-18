class Solution:
    def climbStairs(self, n):
        """
        :type n: int
        :rtype: int
        """
        DP = [0, 1, 2]
        for i in range(3, n + 1):
            DP.append(DP[-1] + DP[-2])
        return DP[n]