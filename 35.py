class Solution:
    def searchInsert(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        if nums == [] or nums[0] >= target:
            return 0
        if nums[-1] < target:
            return len(nums)
        low = 0
        high = len(nums) - 1
        while low < high:
            mid = int((low + high) / 2)
            if nums[mid] < target:
                low = mid + 1
            elif nums[mid] > target:
                high = mid
            else:
                return mid
        return low