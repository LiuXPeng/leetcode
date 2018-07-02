class Solution:
    def nextPermutation(self, nums):
        """
        :type nums: List[int]
        :rtype: void Do not return anything, modify nums in-place instead.
        """
        n = len(nums)
        for i in range(n - 1, 0, -1):
            if nums[i] > nums[i - 1]:
                temp = nums[i - 1]
                for j in range(n - 1, i - 1, -1):
                    if nums[j] > temp:
                        nums[i - 1] = nums[j]
                        nums[j] = temp
                        break
                for j in range((n - i) // 2):
                    temp = nums[i + j]
                    nums[i + j] = nums[n - j - 1]
                    nums[n - j - 1] = temp
                return
        for i in range(n // 2):
            temp = nums[i]
            nums[i] = nums[n - i - 1]
            nums[n - i - 1] = temp
        return