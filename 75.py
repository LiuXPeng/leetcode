class Solution:
    def sortColors(self, nums):
        """
        :type nums: List[int]
        :rtype: void Do not return anything, modify nums in-place instead.
        """
        low = 0
        high = len(nums) - 1
        i = 0
        while i <=high:#如果是<,nums[high]这个数并没有被判断
            if nums[i] == 0:
                nums[i] = nums[low]
                nums[low] = 0
                low += 1
                i += 1
            elif nums[i] == 1:
                i += 1
            else:
                nums[i] = nums[high]
                nums[high] = 2
                high -= 1