class Solution:
    def subsetsWithDup(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        if len(nums) == 0:
            return [[]]
        nums.sort()
        res = [[], [nums[0]]]
        temp = [[nums[0]]]
        for i in range(1, len(nums)):
            if nums[i] == nums[i - 1]:
                for L in temp:
                    L.append(nums[i])
            else:
                temp = copy.deepcopy(res)
                for L in temp:
                    L.append(nums[i])
            res = res + copy.deepcopy(temp)
        return res