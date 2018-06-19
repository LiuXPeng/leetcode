class Solution:
    def maxSubArray(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        res = nums[0]
        curSum = nums[0]
        for i in range(1, len(nums)):          
            if curSum > 0:
                curSum += nums[i]
            else:
                curSum = nums[i]
            if curSum > res:
                res = curSum
        return res