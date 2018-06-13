class Solution:
    def removeDuplicates(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        if len(nums) == 0:
            return 0
        mark = nums[0]
        j = 1
        for i in range(1, len(nums)):
            if nums[i] != mark:
                mark = nums[j] = nums[i]
                j = j + 1
        return j