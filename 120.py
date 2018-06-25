class Solution:
    def minimumTotal(self, triangle):
        """
        :type triangle: List[List[int]]
        :rtype: int
        """
        path = [1000, triangle[0][0]]
        print(path)
        for i in range(1, len(triangle)):
            path.append(path[-1] + triangle[i][-1])
            for j in range(i, 0, -1):
                path[j] = triangle[i][j - 1] + min(path[j], path[j - 1])
            print(path)
        res = path[0]
        for i in path:
            if i < res:
                res = i
        return res