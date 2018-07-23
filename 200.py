class Solution(object):
    def numIslands(self, grid):
        """
        :type grid: List[List[str]]
        :rtype: int
        """
        len1 = len(grid)
        if len1 == 0:
            return 0
        len2 = len(grid[0])
        if len2 == 0:
            return 0
        def dfs(m, n):
            if grid[m][n] == '0':
                return
            grid[m][n] = '0'
            if m > 0:
                dfs(m - 1, n)
            if m < len1 - 1:
                dfs(m + 1, n)
            if n > 0:
                dfs(m, n - 1)
            if n < len2 - 1:
                dfs(m, n + 1)
            return
        res = 0
        for i in range(len1):
            for j in range(len2):
                if grid[i][j] == '1':
                    res += 1
                    dfs(i, j)
        return res