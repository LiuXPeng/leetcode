class Solution:
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        half = []
        half.append(target - nums[0])
        for i in range(1, len(nums)):
            if nums[i] in half:
                 return [half.index(nums[i]), i]
            half.append(target - nums[i])
        return