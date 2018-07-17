class Solution:
    def permute(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        if not nums:
            return [[]]
        res = []
        n = len(nums)
        for i in range(n):
            for j in self.permute(nums[:i] + nums[i+1:]):
                res.append([nums[i]] + j)
        return res