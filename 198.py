class Solution(object):
    def rob(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        if len(nums) < 3:
            res = 0
            for i in nums:
                if i > res:
                    res = i
            return res
        DP = []
        DP.append(nums[0])
        DP.append(nums[1])
        DP.append(nums[0] + nums[2])
        res = DP[1]
        if DP[2] > res:
            res = DP[2]
        for i in range(3, len(nums)):
            DP.append(nums[i] + max(DP[i-2], DP[i-3]))
            res = max(DP[-1], res)
        return res