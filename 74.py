class Solution:
    def searchMatrix(self, matrix, target):
        """
        :type matrix: List[List[int]]
        :type target: int
        :rtype: bool
        """
        if len(matrix) == 0 or len(matrix[0]) == 0:
            return False
        left = low = 0
        high = len(matrix) - 1
        right = len(matrix[0]) - 1
        while low < high:
            mid = (low + high + 1) // 2
            if matrix[mid][0] <= target:
                low = mid
            else:
                high = mid - 1
        while left < right:
            mid = (left + right + 1) // 2
            if matrix[low][mid] <= target:
                left = mid
            else:
                right = mid - 1
        return matrix[low][right] == target