class Solution:
    def combine(self, n, k):
        """
        :type n: int
        :type k: int
        :rtype: List[List[int]]
        """
        if k > n:
            return False
        def dfs(m, n, k):
            res = []
            if k == 1:
                for i in range(m, n):
                    res.append([i])
                return res
            for i in range(m, n - k + 1):
                for temp in dfs(i+1, n, k - 1):
                    res.append([i] + temp)
            return res
        return dfs(1, n + 1, k)