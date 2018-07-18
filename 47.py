class Solution:
    def permuteUnique(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        if not nums:
            return [[]]
        nums.sort()
        res = []
        pre = float('inf')
        for i in range(len(nums)):
            if nums[i] == pre:
                continue
            pre = nums[i]
            temp = self.permuteUnique(nums[:i] + nums[i+1:])
            for j in temp:
                res.append([pre] + j)
        return res