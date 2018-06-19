class Solution:
    def rotate(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: void Do not return anything, modify nums in-place instead.
        """
        if len(nums) <= 1 or (k % len(nums) == 0):
            return
        
        for i in range((len(nums) - k % len(nums)) // 2):
            temp = nums[i]
            nums[i] = nums[len(nums) - k % len(nums) - 1 - i]
            nums[len(nums) - k % len(nums) - 1 - i] = temp
            
        for i in range(k % len(nums) // 2):
            temp = nums[i + len(nums) - k % len(nums)]
            nums[i + len(nums) - k % len(nums)] = nums[len(nums) - 1 - i]
            nums[len(nums) - 1 - i] = temp
            
        for i in range(len(nums) // 2):
            temp = nums[i]
            nums[i] = nums[len(nums) - 1 - i]
            nums[len(nums) - 1 - i] = temp
           
        return