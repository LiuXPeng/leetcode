class Solution:
    def minPathSum(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: int
        """
        m = len(grid)
        n = len(grid[0])
        cost = [[None for col in range(n)] for row in range(m)]
        cost[0][0] = grid[0][0]
        #初始第一行和第一列
        for i in range(1, n):
            cost[0][i] = cost[0][i - 1] + grid[0][i]
        for i in range(1, m):
            cost[i][0] = cost[i - 1][0] + grid[i][0]
        for k in range(2, m + n - 1):
            for i in range(1, m):
                j = k - i
                if j >= n:
                    continue
                cost[i][j] = grid[i][j] + min(cost[i - 1][j], cost[i][j - 1])
                if j == 1:
                    break
        print(cost)
        return cost[m - 1][n - 1]