#有复杂度为n的办法
class Solution:
    def twoSum(self, numbers, target):
        """
        :type numbers: List[int]
        :type target: int
        :rtype: List[int]
        """
        if len(numbers) <= 1:
            return
        high = len(numbers) - 1
        cur = 0
        while cur < high:
            low = cur + 1
            mark = target - numbers[cur]
            while low <= high:
                mid = (low + high) // 2
                if numbers[mid] == mark:
                    return [cur + 1, mid + 1]
                elif numbers[mid] > mark:
                    high = mid - 1
                else:
                    low = mid + 1
            cur += 1
        return