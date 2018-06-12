class Solution:
    def removeDuplicates(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        mark = None
        i = 0
        while i < len(nums):
            if nums[i] == mark:
                del nums[i]
            else:
                mark = nums[i]
                i = i + 1
        return len(nums)