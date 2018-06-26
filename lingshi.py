
def searchMatrix(matrix, target):
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
        mid = (low + high) // 2
        if matrix[mid][0] < target:
            low = mid + 1
        else:
            high = mid
    while left < right:
        mid = (left + right) // 2
        if matrix[low][mid] < target:
            left = mid + 1
        else:
            right = mid
    print(left, low)
    return matrix[left][low] == target

print(searchMatrix([[1, 1]], 2))