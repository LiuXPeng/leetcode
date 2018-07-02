class Solution:
    def canJump(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        n = len(nums)
        label = 0
        for i in range(n):
            if i <= label and nums[i] + i > label:
                label = nums[i] + i
        return label >= n - 1