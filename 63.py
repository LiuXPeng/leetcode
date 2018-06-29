class Solution:
    def uniquePathsWithObstacles(self, obstacleGrid):
        """
        :type obstacleGrid: List[List[int]]
        :rtype: int
        """
        if len(obstacleGrid) == 0:
            return 0
        if len(obstacleGrid[0]) == 0:
            return 0
        DP = [[0 for x in range(len(obstacleGrid[0]))] for y in range(len(obstacleGrid))]
        for i in range(len(obstacleGrid)):
            if obstacleGrid[i][0] == 0:
                DP[i][0] = 1
            else:
                break
        for i in range(len(obstacleGrid[0])):
            if obstacleGrid[0][i] == 0:
                DP[0][i] = 1
            else:
                break
        for i in range(1, len(obstacleGrid)):
            for j in range(1, len(obstacleGrid[0])):
                if obstacleGrid[i][j] != 1:
                    DP[i][j] = DP[i - 1][j] + DP[i][j - 1]
        return DP[-1][-1]