class Solution:
    def uniquePaths(self, m, n):
        """
        :type m: int
        :type n: int
        :rtype: int
        """
        if m < n:
            k = m
        else:
            k = n
        res = 1
        for i in range(1, k):
            res = res * (m + n - 1 - i) / i
        return int(res)